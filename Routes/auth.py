# Routes/auth.py

from flask import Blueprint, request, jsonify
from Model.colaborador import Colaborador
from Model.gestor import Gestor
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

    if not colaborador or colaborador.password != password:
        return jsonify({"mensagem": "Credenciais inválidas"}), 401

    # --- Início da Lógica Modificada ---

    # 2. Prepara o objeto de usuário para o retorno
    user_info = {
        "id_colaborador": colaborador.id,
        "nome": colaborador.nome,
        "email": colaborador.email,
        "is_gestor": False,
        "id_gestor": None  # Inicia como nulo
    }

    # 3. Verifica se o colaborador é um gestor
    gestor = Gestor.query.filter_by(colaborador_id=colaborador.id).first()
    if gestor:
        user_info["is_gestor"] = True
        user_info["id_gestor"] = gestor.id # Adiciona o ID do gestor

    # --- Fim da Lógica Modificada ---

    # Cria o token de acesso
    access_token = create_access_token(identity=colaborador.id)
    
    # 4. Retorna o token e os dados detalhados do usuário
    return jsonify(
        access_token=access_token,
        user=user_info
    )