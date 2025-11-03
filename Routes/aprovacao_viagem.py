from flask import Blueprint, request, jsonify
from Controller.aprovacao_viagem import *

aprovacaoviagem_blueprint = Blueprint('aprovacao-viagem', __name__, url_prefix='/api')

@aprovacaoviagem_blueprint.route('/aprovacao', methods=['POST'])
def cadastrar_aprovacao():
    form_aprovacao = request.get_json()
    aprovacao = criar_aprovacaoViagem(form_aprovacao)
    return jsonify(aprovacao), aprovacao['status_code']

@aprovacaoviagem_blueprint.route('/aprovacao/lista', methods=['GET'])
def listar_aprovacao():
    aprovacao = listar_todas_aprovacoes()
    return jsonify(aprovacao), aprovacao['status_code']

@aprovacaoviagem_blueprint.route('/aprovacao/<int:id>', methods=['GET'])
def get_aprovacao(id):
    aprovacao = get_detalhe_aprovacao(id)
    return jsonify(aprovacao), aprovacao['status_code']