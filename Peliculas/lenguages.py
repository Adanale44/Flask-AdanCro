from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguage',__name__, url_prefix='/lenguages')
@bp. route('/')
def lenguage():
    consulta = """
    SELECT name FROM language
    ORDER by name ASC
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguages = res.fetchall()
    pagina = render_template('lenguages.html',
                            lenguages=lista_lenguages)
    return pagina