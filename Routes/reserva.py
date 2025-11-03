# Routes/reserva.py

from flask import Blueprint, request, jsonify
from Model.reserva import Reserva
from config.config import db # Importar 'db' da configuração

reserva_bp = Blueprint('reserva_bp', __name__, url_prefix='/api')

# Criar uma nova reserva
@reserva_bp.route('/reserva/cadastro', methods=['POST'])
def criar_reserva():
    dados = request.json
    try:
        nova_reserva = Reserva(
            viagem_id=dados['viagem_id'],
            colaborador_id=dados.get('colaborador_id'), # Opcional
            tipo=dados['tipo'],
            fornecedor=dados.get('fornecedor'),
            data_reserva=dados.get('data_reserva'), # Pode usar default
            codigo_reserva=dados.get('codigo_reserva'),
            valor=dados.get('valor')
        )
        db.session.add(nova_reserva)
        db.session.commit()
        return jsonify(nova_reserva.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao criar reserva", "error": str(e)}), 400

# Listar todas as reservas de uma viagem
@reserva_bp.route('/reserva/viagem/<int:id_viagem>', methods=['GET'])
def listar_reservas_viagem(id_viagem):
    reservas = Reserva.query.filter_by(viagem_id=id_viagem).all()
    return jsonify([r.to_dict() for r in reservas])

# Obter detalhes de uma reserva
@reserva_bp.route('/reserva/<int:id>', methods=['GET'])
def obter_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    return jsonify(reserva.to_dict())

# Atualizar uma reserva
@reserva_bp.route('/reserva/<int:id>', methods=['PUT'])
def atualizar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    dados = request.json
    
    try:
        reserva.viagem_id = dados.get('viagem_id', reserva.viagem_id)
        reserva.colaborador_id = dados.get('colaborador_id', reserva.colaborador_id)
        reserva.tipo = dados.get('tipo', reserva.tipo)
        reserva.fornecedor = dados.get('fornecedor', reserva.fornecedor)
        reserva.data_reserva = dados.get('data_reserva', reserva.data_reserva)
        reserva.codigo_reserva = dados.get('codigo_reserva', reserva.codigo_reserva)
        reserva.valor = dados.get('valor', reserva.valor)
        
        db.session.commit()
        return jsonify(reserva.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao atualizar reserva", "error": str(e)}), 400

# Deletar uma reserva
@reserva_bp.route('/reserva/<int:id>', methods=['DELETE'])
def deletar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    try:
        db.session.delete(reserva)
        db.session.commit()
        return jsonify({"mensagem": "Reserva removida com sucesso"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao remover reserva", "error": str(e)}), 500