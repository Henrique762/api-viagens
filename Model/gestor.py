from config.config import db


class Gestor(db.Model):
    __tablename__ = "gestor"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id', ondelete="CASCADE"), nullable=False)



