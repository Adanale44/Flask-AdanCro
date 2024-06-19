@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT first_name, last_name FROM actor
        WHERE actor_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    actor = res.fetchone()
    consulta2 = """
        SELECT title as titulo, f.film_id FROM film f
        JOIN film_actor fil on f.film_id = fil.film_id
        WHERE fil.actor_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaActores = templates("detalles_actores.html",
                                  actor=actor,
                                  peliculas=lista_peliculas)
    return paginaActores