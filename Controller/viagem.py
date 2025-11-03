from datetime import datetime, date
from Model.viagem import adicionar_viagem, alterar_viagem, deletar_viagem, listar_viagens, obter_viagem, viagens_por_colaborador


def validacao_colaborador_id(form):
    if "colaborador_id" not in form:
        raise ValueError("Campo 'colaborador_id' não informado.")
    if form['colaborador_id'] is None:
        raise ValueError("Campo 'colaborador_id' está vazio.")
    if not isinstance(form['colaborador_id'], int):
        raise ValueError("Campo 'colaborador_id' deve ser um número inteiro.")
    return form['colaborador_id']


def validacao_origem(form):
    if "origem" not in form:
        raise ValueError("Campo 'origem' não informado.")
    if form['origem'] is None:
        raise ValueError("Campo 'origem' está vazio.")
    if not isinstance(form['origem'], str):
        raise ValueError("Campo 'origem' deve ser uma String.")
    if len(form['origem']) > 255:
        raise ValueError("Campo 'origem' deve ter no máximo 255 caracteres.")
    return form['origem']


def validacao_destino(form):
    if "destino" not in form:
        raise ValueError("Campo 'destino' não informado.")
    if form['destino'] is None:
        raise ValueError("Campo 'destino' está vazio.")
    if not isinstance(form['destino'], str):
        raise ValueError("Campo 'destino' deve ser uma String.")
    if len(form['destino']) > 255:
        raise ValueError("Campo 'destino' deve ter no máximo 255 caracteres.")
    return form['destino']


def validacao_data_inicio(form):
    if "data_inicio" not in form:
        raise ValueError("Campo 'data_inicio' não informado.")
    if form['data_inicio'] is None:
        raise ValueError("Campo 'data_inicio' está vazio.")

    if isinstance(form['data_inicio'], (datetime, date)):
        return form['data_inicio'] if isinstance(form['data_inicio'], date) else form['data_inicio'].date()
    try:
        return datetime.strptime(form['data_inicio'], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de 'data_inicio' inválido. Use 'YYYY-MM-DD'.")


def validacao_data_fim(form):
    if "data_fim" not in form:
        raise ValueError("Campo 'data_fim' não informado.")
    if form['data_fim'] is None:
        raise ValueError("Campo 'data_fim' está vazio.")

    if isinstance(form['data_fim'], (datetime, date)):
        data_fim = form['data_fim'] if isinstance(form['data_fim'], date) else form['data_fim'].date()
    else:
        try:
            data_fim = datetime.strptime(form['data_fim'], "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de 'data_fim' inválido. Use 'YYYY-MM-DD'.")

    if "data_inicio" in form:
        data_inicio = form['data_inicio']
        if isinstance(data_inicio, str):
            try:
                data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Formato de 'data_inicio' inválido. Use 'YYYY-MM-DD'.")
        elif isinstance(data_inicio, datetime):
            data_inicio = data_inicio.date()

        if data_fim < data_inicio:
            raise ValueError("Campo 'data_fim' não pode ser menor que 'data_inicio'.")

    return data_fim


def validacao_motivo(form):
    if "motivo" not in form:
        raise ValueError("Campo 'motivo' não informado.")
    if form['motivo'] is None:
        raise ValueError("Campo 'motivo' está vazio.")
    if not isinstance(form['motivo'], str):
        raise ValueError("Campo 'motivo' deve ser uma String.")
    if len(form['motivo']) > 255:
        raise ValueError("Campo 'motivo' deve ter no máximo 255 caracteres.")
    return form['motivo']


def validacao_status(form):
    if "status" not in form:
        return "Solicitada"
    if form['status'] is None:
        raise ValueError("Campo 'status' está vazio.")
    if not isinstance(form['status'], str):
        raise ValueError("Campo 'status' deve ser uma String.")
    if len(form['status']) > 255:
        raise ValueError("Campo 'status' deve ter no máximo 255 caracteres.")
    return form['status']


def validacao_form_viagem(form):
    errors = {}

    try:
        form['colaborador_id'] = validacao_colaborador_id(form)
    except ValueError as e:
        errors['colaborador_id'] = str(e)

    try:
        form['origem'] = validacao_origem(form)
    except ValueError as e:
        errors['origem'] = str(e)

    try:
        form['destino'] = validacao_destino(form)
    except ValueError as e:
        errors['destino'] = str(e)

    try:
        form['data_inicio'] = validacao_data_inicio(form)
    except ValueError as e:
        errors['data_inicio'] = str(e)

    try:
        form['data_fim'] = validacao_data_fim(form)
    except ValueError as e:
        errors['data_fim'] = str(e)

    try:
        form['motivo'] = validacao_motivo(form)
    except ValueError as e:
        errors['motivo'] = str(e)

    try:
        form['status'] = validacao_status(form)
    except ValueError as e:
        errors['status'] = str(e)

    if errors:
        return errors
    else:
        return True


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

    dados = form

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