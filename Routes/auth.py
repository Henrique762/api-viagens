# Routes/auth.py

from flask import Blueprint, request, jsonify
from Model.colaborador import Colaborador
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api')

@auth_bp.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    password = dados.get('password')

    if not email or not password:
        return jsonify({"mensagem": "Email e senha são obrigatórios"}), 400

    colaborador = Colaborador.query.filter_by(email=email).first()

    # Alterado: Compara a senha em texto puro diretamente
    if not colaborador or colaborador.password != password:
        return jsonify({"mensagem": "Credenciais inválidas"}), 401

    # Cria o token de acesso
    access_token = create_access_token(identity=colaborador.id)
    return jsonify(access_token=access_token)