import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ...

class Desenvolvimento(Config):
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Producao(Config):
    ENV = "production"
    
class Teste(Config):
    ENV = "testing"
    
config = {
    "development": Desenvolvimento,
    "production":  Producao,
    "testing": Teste
}