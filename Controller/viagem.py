from Model.viagem import adicionar_viagem, alterar_viagem, deletar_viagem, listar_viagens, obter_viagem, viagens_por_colaborador
from Validators.validator_viagem import validacao_form_viagem


def criar_viagem(form):
    result_validacao = validacao_form_viagem(form)

    if isinstance(result_validacao, dict):
        return {
            'message': 'Erro ao criar viagem',
            'errors': result_validacao,
            'status_code': 400
        }

    dados = form

    try:
        viagem = adicionar_viagem(dados)
        return {
            'message': 'Viagem criada com sucesso',
            'viagem_id': viagem.id,
            'status_code': 201
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao criar viagem',
            'error': str(e),
            'status_code': 500
        }


def editar_viagem(id, form):
    result_validacao = validacao_form_viagem(form)

    if isinstance(result_validacao, dict):  # houve erro de validação
        return {
            'message': 'Erro ao editar viagem',
            'errors': result_validacao,
            'status_code': 400
        }

    viagem = obter_viagem(id)
    if not viagem:
        return {
            'message': 'Viagem não encontrada',
            'status_code': 404
        }

    try:
        viagem = alterar_viagem(form, id)
        return {
            'message': 'Viagem editada com sucesso',
            'viagem_id': viagem.id,
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao editar viagem',
            'error': str(e),
            'status_code': 500
        }


def remover_viagem(id):
    viagem = obter_viagem(id)
    if not viagem:
        return {
            'message': 'Viagem não encontrada',
            'status_code': 404
        }

    try:
        deletar_viagem(id)
        return {
            'message': 'Viagem removida com sucesso',
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao remover viagem',
            'error': str(e),
            'status_code': 500
        }


def listar_todas_viagens():
    try:
        viagens = listar_viagens()
        return {
            'message': 'Lista de viagens recuperada com sucesso',
            'viagens': [
                {
                    "id": v.id,
                    "colaborador_id": v.colaborador_id,
                    "origem": v.origem,
                    "destino": v.destino,
                    "data_inicio": str(v.data_inicio),
                    "data_fim": str(v.data_fim),
                    "motivo": v.motivo,
                    "status": v.status
                }
                for v in viagens
            ],
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao listar viagens',
            'error': str(e),
            'status_code': 500
        }


def obter_detalhe_viagem(id):
    try:
        viagem = obter_viagem(id)
        if not viagem:
            return {
                'message': 'Viagem não encontrada',
                'status_code': 404
            }

        return {
            'message': 'Viagem encontrada com sucesso',
            'viagem': {
                "id": viagem.id,
                "colaborador_id": viagem.colaborador_id,
                "origem": viagem.origem,
                "destino": viagem.destino,
                "data_inicio": str(viagem.data_inicio),
                "data_fim": str(viagem.data_fim),
                "motivo": viagem.motivo,
                "status": viagem.status
            },
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao buscar viagem',
            'error': str(e),
            'status_code': 500
        }


def obter_viagens_por_colaborador(id_colaborador):
    viagens_obj = viagens_por_colaborador(id_colaborador)
    
    lista_viagens = [
        {
            "id": v.id,
            "colaborador_id": v.colaborador_id,
            "origem": v.origem,
            "destino": v.destino,
            "data_inicio": str(v.data_inicio),
            "data_fim": str(v.data_fim),
            "motivo": v.motivo,
            "status": v.status
        }
        for v in viagens_obj
    ]
    
    return {
        "status_code": 200,
        "message": "Lista de viagens recuperada com sucesso",
        "viagens": lista_viagens
    }

