from config.config import db
from sqlalchemy import Time, Date

class Colaborador(db.Model):
    __tablename__ = "colaborador"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id', ondelete="CASCADE"), nullable=False)
    area = db.Column(db.Integer, db.ForeignKey('area.id', ondelete="CASCADE"), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    data_nasc = db.Column(Date, nullable=False)
    data_adm = db.Column(Date, nullable=False)
    data_dem = db.Column(Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    gestao = db.Column(db.Integer, db.ForeignKey('gestor.id', ondelete="CASCADE"), nullable=True)