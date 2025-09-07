from Validators.validator_aprovacao import validacao_form_aprovacao, validacao_id_viagem
from Model.aprovacao_viagem import createAprovacaoViagem, getAprovacaoViagem


def criar_aprovacaoViagem(form):
    result_validacao = validacao_form_aprovacao(form)

    if isinstance(result_validacao, dict):
        return {
            'message': 'Erro ao criar aprovação da viagem',
            'errors': result_validacao,
            'status_code': 400
        }

    try:
        viagem = createAprovacaoViagem(form)
        return {
            'message': 'Aprovação da viagem criada com sucesso',
            'viagem_id': viagem.id,
            'status_code': 201
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao criar aprovação da viagem',
            'error': str(e),
            'status_code': 500
        }
        
def listar_todas_aprovacoes():
    try:
        aprovacoes = getAprovacaoViagem()
        return {
            'message': 'Lista de aprovação recuperada com sucesso',
            'aprovacoes': [
                {
                    "id": a.id,
                    "colaborador_id": a.colaborador_id,
                    "gestor_id": a.gestor_id,
                    "viagem_id": a.viagem_id,
                    "date": a.date,
                    "status": a.status
                }
                for a in aprovacoes
            ],
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao listar aprovações de viagens',
            'error': str(e),
            'status_code': 500
        }
        
def get_detalhe_aprovacao(idViagem):
    result_validacao =  validacao_id_viagem(idViagem)
    if isinstance(result_validacao, dict):
        return {
            'message': 'Erro ao consultar detalhes da aprovação da viagem',
            'errors': result_validacao,
            'status_code': 400
    }
        
    try:
        aprovacao = getAprovacaoViagem(idViagem)
        
        if not aprovacao:
            return {
                'message': 'Aprovação de viagem não encontrada',
                'status_code': 404
            }
            
        return {
            'message': 'Aprovação recuperada com sucesso',
            'aprovacoes': 
                {
                    "id": aprovacao.id,
                    "colaborador_id": aprovacao.colaborador_id,
                    "gestor_id": aprovacao.gestor_id,
                    "viagem_id": aprovacao.viagem_id,
                    "date": aprovacao.date,
                    "status": aprovacao.status
                }
            ,
            'status_code': 200
        }
    except Exception as e:
        return {
            'message': 'Erro interno ao buscar aprovação de viagem',
            'error': str(e),
            'status_code': 500
        }