from flask import jsonify, request
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

    def to_dict(self):
        return {
            "id": self.id,
            "cargo_id": self.cargo_id,
            "area": self.area,
            "nome": self.nome,
            "data_nasc": self.data_nasc.isoformat(),
            "data_adm": self.data_adm.isoformat(),
            "data_dem": self.data_dem.isoformat(),
            "status": self.status,
            "gestao": self.gestao
        }
    
    def criar_colaborador():
        dados = request.json
        colaborador = Colaborador(
            cargo_id=dados['cargo_id'],
            area=dados['area'],
            nome=dados['nome'],
            data_nasc=dados['data_nasc'],
            data_adm=dados['data_adm'],
            data_dem=dados['data_dem'],
            status=dados.get('status', True),
            gestao=dados.get('gestao')
        )
        db.session.add(colaborador)
        db.session.commit()
        return jsonify(colaborador.to_dict()), 201

    def listar_colaboradores():
        colaboradores = Colaborador.query.all()
        return jsonify([c.to_dict() for c in colaboradores])

    def obter_colaborador(id):
        colaborador = Colaborador.query.get_or_404(id)
        return jsonify(colaborador.to_dict())

    def atualizar_colaborador(id):
        colaborador = Colaborador.query.get_or_404(id)
        dados = request.json
        for campo in ['cargo_id', 'area', 'nome', 'data_nasc', 'data_adm', 'data_dem', 'status', 'gestao']:
            if campo in dados:
                setattr(colaborador, campo, dados[campo])
        db.session.commit()
        return jsonify(colaborador.to_dict())

    def deletar_colaborador(id):
        colaborador = Colaborador.query.get_or_404(id)
        db.session.delete(colaborador)
        db.session.commit()
        return jsonify({"mensagem": "Colaborador removido com sucesso"})