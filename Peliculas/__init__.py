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


    