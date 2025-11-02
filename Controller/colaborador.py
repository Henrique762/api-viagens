from datetime import datetime, date
from Model.colaborador import db, Colaborador


def validar_nome(form):
    if "nome" not in form:
        raise ValueError("Campo 'nome' não informado.")
    
    if form['nome'] is None or form['nome'].strip() == "":
        raise ValueError("Campo 'nome' está vazio.")
    
    if not isinstance(form['nome'], str):
        raise ValueError("Campo 'nome' deve ser uma String.")
    
    if len(form['nome']) > 255:
        raise ValueError("Campo 'nome' deve ter no máximo 255 caracteres.")
    return form['nome'].strip()

def validar_cargo_id(form):
    if "cargo_id" not in form:
        raise ValueError("Campo 'cargo_id' não informado.")
    
    if form['cargo_id'] is None:
        raise ValueError("Campo 'cargo_id' está vazio.")
    
    if not isinstance(form['cargo_id'], int):
        raise ValueError("Campo 'cargo_id' deve ser um número inteiro.")
    return form['cargo_id']

def validar_area(form):
    if "area" not in form:
        raise ValueError("Campo 'area' não informado.")
    
    if form['area'] is None:
        raise ValueError("Campo 'area' está vazio.")
    
    if not isinstance(form['area'], int):
        raise ValueError("Campo 'area' deve ser um número inteiro.")
    return form['area']

def validar_gestao(form):
    if "gestao" not in form or form['gestao'] is None:
        return None
    
    if not isinstance(form['gestao'], int):
        raise ValueError("Campo 'gestao' deve ser um número inteiro.")
    return form['gestao']

def validar_data(field_name, form):
    if field_name not in form:
        raise ValueError(f"Campo '{field_name}' não informado.")
    
    if form[field_name] is None:
        raise ValueError(f"Campo '{field_name}' está vazio.")
    
    if isinstance(form[field_name], (datetime, date)):
        return form[field_name] if isinstance(form[field_name], date) else form[field_name].date()
    try:
        return datetime.strptime(form[field_name], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Formato de '{field_name}' inválido. Use 'YYYY-MM-DD'.")

def validar_status(form):
    if "status" not in form:
        return True
    if form['status'] is None:
        raise ValueError("Campo 'status' está vazio.")
    
    if not isinstance(form['status'], bool):
        raise ValueError("Campo 'status' deve ser um valor booleano.")
    return form['status']

def validacao_form_colaborador(form):
    errors = {}

    try:
        form['nome'] = validar_nome(form)
    except ValueError as e:
        errors['nome'] = str(e)

    try:
        form['cargo_id'] = validar_cargo_id(form)
    except ValueError as e:
        errors['cargo_id'] = str(e)

    try:
        form['area'] = validar_area(form)
    except ValueError as e:
        errors['area'] = str(e)

    try:
        form['gestao'] = validar_gestao(form)
    except ValueError as e:
        errors['gestao'] = str(e)

    try:
        form['data_nasc'] = validar_data("data_nasc", form)
    except ValueError as e:
        errors['data_nasc'] = str(e)

    try:
        form['data_adm'] = validar_data("data_adm", form)
    except ValueError as e:
        errors['data_adm'] = str(e)

    try:
        form['data_dem'] = validar_data("data_dem", form)
    except ValueError as e:
        errors['data_dem'] = str(e)

    # Lógica de datas
    if "data_nasc" in form and "data_adm" in form and "data_dem" in form:
        if form['data_nasc'] >= form['data_adm']:
            errors['data_nasc'] = "Data de nascimento deve ser anterior à data de admissão."
        if form['data_adm'] >= form['data_dem']:
            errors['data_adm'] = "Data de admissão deve ser anterior à data de demissão."

    try:
        form['status'] = validar_status(form)
    except ValueError as e:
        errors['status'] = str(e)

    return errors if errors else True