from config.config import db

class Cargo(db.Model):
    __tablename__ = "cargo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    cargo = db.Column(db.String(255), nullable=False)