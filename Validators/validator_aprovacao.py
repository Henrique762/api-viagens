from Validators.validator_field import *

def validacao_form_aprovacao(form):
    errors = {}

    try:
        form['colaborador_id'] = validacao_colaborador_id(form)
    except ValueError as e:
        errors['colaborador_id'] = str(e)

    try:
        form['gestor_id'] = validacao_gestor_id(form)
    except ValueError as e:
        errors['gestor_id'] = str(e)
        
    try:
        form['viagem_id'] = validacao_viagem_id(form)
    except ValueError as e:
        errors['viagem_id'] = str(e)
        
    try:
        form['data_inicio'] = validacao_data(form)
    except ValueError as e:
        errors['data_inicio'] = str(e)

    try:
        form['status'] = validacao_status(form)
    except ValueError as e:
        errors['status'] = str(e)

    if errors:
        return errors
    else:
        return True
    
def validacao_id_viagem(id):
    errors = {}
    try:
        id = validacao_viagem_id(id)
    except ValueError as e:
        errors['viagem_id'] = str(e)
        
    if errors:
        return errors
    else:
        return True