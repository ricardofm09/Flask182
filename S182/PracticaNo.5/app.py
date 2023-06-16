from flask import Flask 


#inicializacion del servido Flask 
app= Flask(__name__)

#Declaracion de rutas


# ruta se compone del nombre y funcion

# Ruta Index http://localhost:5000
@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/guardar')
def guardar():
    return "se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "se elimino el album en la BD"

# Ejecucion de servidor 
if __name__==  'main_':
        app.run(port= 5000)