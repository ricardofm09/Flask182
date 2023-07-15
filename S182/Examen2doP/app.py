from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DB_Floreria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/floreria', methods=['GET', 'POST'])
def floreria():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        curSelect = mysql.connection.cursor()
        curSelect.execute('SELECT * FROM tbFlores WHERE nombre LIKE %s', ('%' + nombre + '%',))
        flores = curSelect.fetchall()
        curSelect.close()

        return render_template('floreria.html', flores=flores)

    return redirect(url_for('index'))

@app.route('/lista_floreria')
def lista_floreria():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFlores')
    flores = curSelect.fetchall()
    curSelect.close()

    return render_template('floreria.html', flores=flores)

@app.route('/eliminar/<int:id>')
def eliminar_flor(id):
    cs = mysql.connection.cursor()
    cs.execute('DELETE FROM tbFlores WHERE id = %s', (id,))
    mysql.connection.commit()
    cs.close()

    flash('Flor eliminada correctamente')
    return redirect(url_for('lista_floreria'))

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_flor(id):
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']
        Vprecio = request.form['txtPrecio']

        cs = mysql.connection.cursor()
        cs.execute('UPDATE tbFlores SET nombre = %s, cantidad = %s, precio = %s WHERE id = %s', (Vnombre, Vcantidad, Vprecio, id))
        mysql.connection.commit()
        cs.close()

        flash('Flor actualizada correctamente')
        return redirect(url_for('lista_floreria'))

    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFlores WHERE id = %s', (id,))
    flor = curSelect.fetchone()
    curSelect.close()

    return render_template('actualizar.html', flor=flor)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']
        Vprecio = request.form['txtPrecio']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tbFlores (nombre, cantidad, precio) VALUES (%s, %s, %s)', (Vnombre, Vcantidad, Vprecio))
        mysql.connection.commit()
        cs.close()

    flash('Flor agregada correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
