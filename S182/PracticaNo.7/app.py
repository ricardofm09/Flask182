
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#inicializacion del servido Flask 
app = Flask(__name__)

#configurarciones de conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "dbflask"

app.secret_key='mysecretkey'

mysql = MySQL(app)

#Declaracion de rutas


# ruta se compone del nombre y funcion

# ruta Index http://localhost:5000
@app.route('/')
def index():
    curSelect= mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta= curSelect.fetchall()
    #print(consulta)

    return render_template('index.html', listAlbums=consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        
        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO albums (titulo, artista, anio) VALUES(%s, %s, %s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
        cs.close()


    flash('Album agregado correctamente') 
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"

# Ejecucion de servidor 
if __name__==  '__main__':
        app.run(port= 5000,debug=True)