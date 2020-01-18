from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def cria_app(config_nome):
    app = Flask(__name__)
    app.template_folder = "temas"
    
    app.config.from_object(config[config_nome])
    
    # registrando plugins
    db.init_app(app)

    # importando rotas e executando as mesmas...
    from app import rotas
    rotas.carrega_rotas(app)
    
    # retornando minha própria aplicação.
    return app

