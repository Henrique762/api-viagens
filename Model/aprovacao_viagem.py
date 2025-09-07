from sqlalchemy import Date
from config.config import db

class AprovacaoViagem(db.Model):
    __tablename__ = "aprovacaoViagem"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    idGestor = db.Column(db.Integer, db.ForeignKey('gestor.id', ondelete="CASCADE"), nullable = False)
    idColaborador = db.Column(db.Integer, db.ForeignKey('colaborador.id', ondelete="CASCADE"), nullable = False)
    idViagem = db.Column(db.Integer, db.ForeignKey('viagem.id', ondelete="CASCADE"), nullable = False)
    date = db.Column(Date, nullable = False)
    status = db.Column(db.String(255), nullable = False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "gestor_id": self.idGestor,
            "colaborador_id": self.idColaborador,
            "viagem_id": self.idViagem,
            "date": self.date.isoformat() if self.date else None,
            "status": self.status
        }
        

def getAprovacaoViagem():
    return AprovacaoViagem.query.all()

def getAprovacaoViagem(idViagem):
    return AprovacaoViagem.query.filter_by(idViagem=idViagem)

def createAprovacaoViagem(data):
    aprovacao = AprovacaoViagem(idGestor = data["gestor_id"], idColaborador = data["colaborador_id"], idViagem = data["viagem_id"], date = data["date"], status = data["status"])
    db.session.add(aprovacao)
    db.session.commit()
    return aprovacao

def deleteAprovacaoViagem(id):
    aprovacao = AprovacaoViagem.query.get(id)

    if not aprovacao:
        return 'Aprovação da viagem inexistente'

    db.session.delete(aprovacao)
    db.session.commit()
    return 'Aprovação da viagem apagada'