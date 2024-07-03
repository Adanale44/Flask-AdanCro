from flask import Blueprint, render_template
from . import db

bp = Blueprint('Peliculas',__name__, url_prefix='/peliculas')

@bp. route('/')
def pelicula():
    consulta = """
     SELECT title AS titulo, film_id from film 
     ORDER by title ASC ;
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_pelis = res.fetchall()
    pagina = render_template('peliculas.html',
                            peliculas=lista_pelis)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT title,rating,release_year,description, film_id from film 
        where film_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    pelicula = res.fetchone()
    consultaa = """
        SELECT last_name, first_name, a.actor_id from film_actor f
        join actor a on f.actor_id = a.actor_id
        where film_id = ?
    """

    res = con.execute(consultaa, (id,))
    lista_actores = res.fetchall()
    pagina = render_template("detallado_actores.html",
                                  pelicula=pelicula,
                                  actores=lista_actores)
    return pagina