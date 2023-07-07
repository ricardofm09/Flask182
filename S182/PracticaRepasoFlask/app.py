from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_fruteria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frutas', methods=['GET', 'POST'])
def frutas():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        curSelect = mysql.connection.cursor()
        curSelect.execute('SELECT * FROM tbFrutas WHERE fruta LIKE %s', ('%' + nombre + '%',))
        frutas = curSelect.fetchall()
        curSelect.close()

        return render_template('frutas.html', frutas=frutas)

    return redirect(url_for('index'))

@app.route('/lista_frutas')
def lista_frutas():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFrutas')
    frutas = curSelect.fetchall()
    curSelect.close()

    return render_template('frutas.html', frutas=frutas)

@app.route('/eliminar/<int:id>')
def eliminar_fruta(id):
    cs = mysql.connection.cursor()
    cs.execute('DELETE FROM tbFrutas WHERE id = %s', (id,))
    mysql.connection.commit()
    cs.close()

    flash('Fruta eliminada correctamente')
    return redirect(url_for('lista_frutas'))

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_fruta(id):
    if request.method == 'POST':
        Vfruta = request.form['txtFruta']
        Vtemporada = request.form['txtTemporada']
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtStock']

        cs = mysql.connection.cursor()
        cs.execute('UPDATE tbFrutas SET fruta = %s, temporada = %s, precio = %s, stock = %s WHERE id = %s', (Vfruta, Vtemporada, Vprecio, Vstock, id))
        mysql.connection.commit()
        cs.close()

        flash('Fruta actualizada correctamente')
        return redirect(url_for('lista_frutas'))

    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFrutas WHERE id = %s', (id,))
    fruta = curSelect.fetchone()
    curSelect.close()

    return render_template('actualizar.html', fruta=fruta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vfruta = request.form['txtFruta']
        Vtemporada = request.form['txtTemporada']
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtStock']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tbFrutas (fruta, temporada, precio, stock) VALUES (%s, %s, %s, %s)', (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()
        cs.close()

    flash('Fruta agregada correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
