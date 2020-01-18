from app import db


class Postagem(db.Model):
    __tablename__ = "postagens"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80))
    texto = db.Column(db.Text)
    

 