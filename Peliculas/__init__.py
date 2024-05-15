from flask import Flask, render_template

app = Flask(__name__)
with app.app_context():
   from . import db
   db.init_app(app) 

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/adan')
def achi():
    return 'Aplicacion con dos rutas' 

@app. route('/actores')
def actor():
    consulta = """
     SELECT first_name,last_name FROM actor
     ORDER BY first_name ;
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    pagina = render_template('actores.html',
                            actores=lista_actores)
    return pagina
     