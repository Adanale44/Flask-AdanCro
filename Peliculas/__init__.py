from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app) 


@app.route('/adan')
def achi():
    return 'Aplicacion con dos rutas' 


from . import actor
app.register_blueprint(actor.bp) 

from . import categorias
app.register_blueprint(categorias.bp) 

from . import lenguages
app.register_blueprint(lenguages.bp) 

from . import peliculas
app.register_blueprint(peliculas.bp) 



    