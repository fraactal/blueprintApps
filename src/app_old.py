from flask import Flask, render_template
import os
import pymysql

app = Flask(__name__)


################## ConfigEvento #########################

'''

@app.route('/getConfigApp', methods = ['GET'])
def getConfigApp():
  try:
    configApp = returnConfig()
    return jsonify({"configApp" : configApp, "mensaje":"Configuración Actual BD"})
  except Exception as ex:
    return jsonify({"Mensaje" : {str(ex)}})


@app.route('/updateConfiguracion', methods = ['PUT'])
def updateConfig():
  try:
    configApp = updateConfiguracion(request.json)
    return jsonify({"mensaje": str(configApp)})
  except Exception as ex:
    return jsonify({"mensaje" : {str(ex)}})

'''


################ Handler Page ########################

@app.route('/about')
def about():
    return render_template('about.html')
    
def PaginaNoEncontrada(error):
    return "<h1>La URL que intentas buscar no existe..</h1>" , 404

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    #app.config.from_object(config['development'])
    app.register_error_handler(404, PaginaNoEncontrada)
    app.run(host='0.0.0.0', port=port)
