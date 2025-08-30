from flask import Blueprint, request, jsonify
from Controller.viagem import criar_viagem, listar_todas_viagens, obter_detalhe_viagem, editar_viagem, remover_viagem, obter_viagens_por_colaborador

viagem_blueprint = Blueprint('viagem', __name__, url_prefix='/api')


@viagem_blueprint.route('/viagem/cadastro', methods=['POST'])
def cadastrar_viagem():
    form_viagem = request.get_json()
    viagem = criar_viagem(form_viagem)
    return jsonify(viagem), viagem['status_code']



@viagem_blueprint.route('/viagem', methods=['GET'])
def listar():
    viagens = listar_todas_viagens()
    return jsonify(viagens), viagens['status_code']



@viagem_blueprint.route('/viagem/<int:id>', methods=['GET'])
def detalhe_viagem(id):
    viagem = obter_detalhe_viagem(id)
    return jsonify(viagem), viagem['status_code']



@viagem_blueprint.route('/viagem/<int:id>', methods=['PUT'])
def editar_viagem_route(id):
    form_viagem = request.get_json()
    viagem = editar_viagem(id, form_viagem)
    return jsonify(viagem), viagem['status_code']


@viagem_blueprint.route('/viagem/<int:id>', methods=['DELETE'])
def remover_viagem_route(id):
    viagem = remover_viagem(id)
    return jsonify(viagem), viagem['status_code']

@viagem_blueprint.route('/viagem/colaborador/<int:id_colaborador>', methods=['GET'])
def viagens_colaborador(id_colaborador):
    resultado = obter_viagens_por_colaborador(id_colaborador)
    return jsonify(resultado), resultado['status_code']
