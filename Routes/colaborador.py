from flask import Blueprint, request, jsonify
from Model.colaborador import db, Colaborador

colaborador_bp = Blueprint('colaborador_bp', __name__, url_prefix='/colaboradores')


@colaborador_bp.route('/', methods=['POST'])
def criar_colaborador():
    dados = request.json
    colaborador = Colaborador(
        cargo_id=dados['cargo_id'],
        area=dados['area'],
        nome=dados['nome'],
        email=dados['email'],
        password=dados['password'],
        data_nasc=dados['data_nasc'],
        data_adm=dados['data_adm'],
        data_dem=dados['data_dem'],
        status=dados.get('status', True),
        gestao=dados.get('gestao')
    )
    db.session.add(colaborador)
    db.session.commit()
    return jsonify(colaborador.to_dict()), 201

@colaborador_bp.route('/colaborador/', methods=['GET'])
def listar_colaboradores():
    colaboradores = Colaborador.query.all()
    return jsonify([c.to_dict() for c in colaboradores])

@colaborador_bp.route('/colaborador/<int:id>', methods=['GET'])
def obter_colaborador(id):
    colaborador = Colaborador.query.get_or_404(id)
    return jsonify(colaborador.to_dict())

@colaborador_bp.route('/colaborador/<int:id>', methods=['PUT'])
def atualizar_colaborador(id):
    colaborador = Colaborador.query.get_or_404(id)
    dados = request.json
    
    campos = ['cargo_id', 'area', 'nome', 'email', 'password', 'data_nasc', 'data_adm', 'data_dem', 'status', 'gestao']
    
    for campo in campos:
        if campo in dados:
            setattr(colaborador, campo, dados[campo])
            

    db.session.commit()
    return jsonify(colaborador.to_dict())

@colaborador_bp.route('/colaborador/<int:id>', methods=['DELETE'])
def deletar_colaborador(id):
    colaborador = Colaborador.query.get_or_404(id)
    db.session.delete(colaborador)
    db.session.commit()
    return jsonify({"mensagem": "Colaborador removido com sucesso"})