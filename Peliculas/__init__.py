from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/Adan')
def achi():
    return 'Aplicacion con dos rutas'