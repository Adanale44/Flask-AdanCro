from flask import Blueprint, render_template
from . import db

bp = Blueprint('categoria',__name__, url_prefix='/categorias')
@bp. route('/')
def actor():
    consulta = """
    SELECT name FROM category
    ORDER by name ASC
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    pagina = render_template('categorias.html',
                            categorias=lista_actores)
    return pagina