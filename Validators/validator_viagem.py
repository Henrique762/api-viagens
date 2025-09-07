from Validators.validator_field import *
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