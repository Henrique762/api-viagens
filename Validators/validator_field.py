from datetime import date, datetime


def validacao_colaborador_id(form):
    if "colaborador_id" not in form:
        raise ValueError("Campo 'colaborador_id' não informado.")
    if form['colaborador_id'] is None:
        raise ValueError("Campo 'colaborador_id' está vazio.")
    if not isinstance(form['colaborador_id'], int):
        raise ValueError("Campo 'colaborador_id' deve ser um número inteiro.")
    return form['colaborador_id']

def validacao_gestor_id(form):
    if "gestor_id" not in form:
        raise ValueError("Campo 'gestor_id' não informado.")
    if form['gestor_id'] is None:
        raise ValueError("Campo 'gestor_id' está vazio.")
    if not isinstance(form['gestor_id'], int):
        raise ValueError("Campo 'gestor_id' deve ser um número inteiro.")
    return form['gestor_id']

def validacao_viagem_id(form):
    if "viagem_id" not in form:
        raise ValueError("Campo 'viagem_id' não informado.")
    if form['viagem_id'] is None:
        raise ValueError("Campo 'viagem_id' está vazio.")
    if not isinstance(form['viagem_id'], int):
        raise ValueError("Campo 'viagem_id' deve ser um número inteiro.")
    return form['viagem_id']

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

def validacao_data(form):
    if "date" not in form:
        raise ValueError("Campo 'data' não informado.")
    if form['date'] is None:
        raise ValueError("Campo 'data' está vazio.")

    if isinstance(form['date'], (datetime, date)):
        return form['date'] if isinstance(form['date'], date) else form['date'].date()
    try:
        return datetime.strptime(form['date'], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de 'data' inválido. Use 'YYYY-MM-DD'.")

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
