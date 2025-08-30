from Model.area import Area
from Model.cargo import Cargo
from Model.colaborador import Colaborador
from Model.gestor import Gestor
from config.config import db


def seed_areas():
    areas = ['financeiro', 'recursos humanos', 'comercial', 'marketing', 'suporte', 'ti', 'operacoes', 'logistica']
    if Area.query.first():
        print("Areas já cadastradas.")
        return

    for nome in areas:
        db.session.add(Area(area=nome))
    db.session.commit()
    print("Areas inseridas com sucesso!")

def seed_cargos():
    cargos = ['estagiario', 'assistente', 'analista', 'coordenador', 'gerente', 'diretor', 'ceo']
    if Cargo.query.first():
        print("Cargos já cadastrados.")
        return

    for nome in cargos:
        db.session.add(Cargo(cargo=nome))
    db.session.commit()
    print("Cargos inseridos com sucesso!")

def seed_all():
    seed_areas()
    seed_cargos()