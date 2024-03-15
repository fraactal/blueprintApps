from flask import Flask, render_template
import os
from blueprint.helloworld.helloworld import helloworld_bp
from blueprint.calculator.calculator import calculator_bp

app = Flask(__name__)
app.register_blueprint(helloworld_bp)
app.register_blueprint(calculator_bp, url_prefix = "/calculator")



#if __name__ == '__main__':
    #app.run(debug=True)
#    app.run(host="0.0.0.0", port=80)


################ Handler Page ########################

@app.route('/about')
def about():
    return render_template('about.html')
    
def PaginaNoEncontrada():
    return "<h1>La URL que intentas buscar no existe..</h1>" , 404

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    #app.config.from_object(config['development'])
    app.register_error_handler(404, PaginaNoEncontrada)
    app.run(host='0.0.0.0', port=port)
