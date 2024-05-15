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