# Routes/gestor.py

from flask import Blueprint, jsonify
from Model.gestor import Gestor
from Model.colaborador import Colaborador
from config.config import db

gestor_bp = Blueprint('gestor_bp', __name__, url_prefix='/api')

# Modificado: A rota agora recebe o ID do colaborador pela URL
@gestor_bp.route('/gestor/<int:colaborador_id>', methods=['POST'])
def criar_gestor(colaborador_id):
    
    # 1. Verificar se o colaborador existe
    # (Usamos o 'colaborador_id' vindo da URL)
    colaborador = Colaborador.query.get(colaborador_id)
    if not colaborador:
        return jsonify({"mensagem": "Colaborador não encontrado"}), 404

    # 2. Verificar se ele já não é um gestor
    gestor_existente = Gestor.query.filter_by(colaborador_id=colaborador_id).first()
    if gestor_existente:
        return jsonify({"mensagem": "Este colaborador já é um gestor"}), 409

    # 3. Criar o novo gestor
    try:
        novo_gestor = Gestor(colaborador_id=colaborador_id)
        db.session.add(novo_gestor)
        db.session.commit()
        
        return jsonify({
            "mensagem": "Colaborador ativado como gestor com sucesso",
            "gestor_id": novo_gestor.id,
            "colaborador_id": novo_gestor.colaborador_id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"mensagem": "Erro interno ao criar gestor", "error": str(e)}), 500