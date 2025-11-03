# Model/reserva.py

from config.config import db
from sqlalchemy import Date, Numeric, func

class Reserva(db.Model):
    __tablename__ = "reserva"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    viagem_id = db.Column(db.Integer, db.ForeignKey('viagem.id', ondelete="CASCADE"), nullable=False)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id'), nullable=True) # Opcional, como solicitado
    
    tipo = db.Column(db.String(100), nullable=False) # Ex: 'Passagem', 'Hotel', 'Outro'
    fornecedor = db.Column(db.String(255), nullable=True)
    data_reserva = db.Column(Date, nullable=False, default=func.current_date())
    codigo_reserva = db.Column(db.String(255), nullable=True)
    valor = db.Column(Numeric(10, 2), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "viagem_id": self.viagem_id,
            "colaborador_id": self.colaborador_id,
            "tipo": self.tipo,
            "fornecedor": self.fornecedor,
            "data_reserva": self.data_reserva.isoformat() if self.data_reserva else None,
            "codigo_reserva": self.codigo_reserva,
            "valor": str(self.valor) if self.valor is not None else None
        }