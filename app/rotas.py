from flask import render_template
from app.modelos import Postagem


def carrega_rotas(app):    
    @app.route("/")
    def inicio():
        postagens = Postagem.query.all()
        return render_template("index.html", postagens=postagens)


    @app.route("/suporte")
    def suporte():
        return render_template("suporte.html")
    