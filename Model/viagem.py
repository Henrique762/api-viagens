from config.config import db
from sqlalchemy import Time, Date

class Viagem(db.Model):
    __tablename__ = "viagem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id', ondelete="CASCADE"), nullable=False)
    origem = db.Column(db.String(255))
    destino = db.Column(db.String(255))
    data_inicio = db.Column(Date, nullable=False)
    data_fim = db.Column(Date, nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False, default='Solicitada')


    def to_dict(self):
        return {
            "id": self.id,
            "colaborador_id": self.colaborador_id,
            "origem": self.origem,
            "destino": self.destino,
            "data_inicio": self.data_inicio.isoformat() if self.data_inicio else None,
            "data_fim": self.data_fim.isoformat() if self.data_fim else None,
            "motivo": self.motivo,
            "status": self.status
        }



def adicionar_viagem(data):
    viagem = Viagem(colaborador_id=data['colaborador_id'], origem =data['origem'], destino =data['destino'], data_inicio=data['data_inicio'], data_fim=data['data_fim'], motivo=data['motivo'])
    db.session.add(viagem)
    db.session.commit()
    return viagem


def alterar_viagem(data, viagem_id):
    viagem = Viagem.query.get(viagem_id)

    if not viagem:
        return 'Viagem inexistente'

    viagem.colaborador_id = data.get('colaborador_id', viagem.colaborador_id)
    viagem.origem = data.get('origem', viagem.origem)
    viagem.destino = data.get('destino', viagem.destino)
    viagem.data_inicio = data.get('data_inicio', viagem.data_inicio)
    viagem.data_fim = data.get('data_fim', viagem.data_fim)
    viagem.motivo = data.get('motivo', viagem.motivo)
    viagem.status = data.get('status', viagem.status)

    db.session.commit()
    return viagem

def deletar_viagem(viagem_id):
    viagem = Viagem.query.get(viagem_id)

    if not viagem:
        return 'Viagem inexistente'

    db.session.delete(viagem)
    db.session.commit()
    return 'Viagem apagada'

def listar_viagens():
    return Viagem.query.all()

def obter_viagem(viagem_id):
    return Viagem.query.get(viagem_id)


def viagens_por_colaborador(id_colaborador):
    viagens = db.session.query(Viagem).filter_by(id=id_colaborador).all()
    print(viagens)
    return viagens