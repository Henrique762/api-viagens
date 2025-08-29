from config.config import db


class Cargo(db.Model):
    __tablename__ = "cargo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    area = db.Column(db.String(255), nullable=False)

def data_area():
    cargo_list = ['estagiario', 'assistente', 'analista', 'coordenador', 'gerente', 'diretor', 'ceo']
    if Cargo.query.first():
        print("Cargos já cadastrados.")
        return

    for nome in cargo_list:
        status = Cargo(nome=nome)
        db.session.add(status)
    
    db.session.commit()
    print("Cargos inseridos com sucesso!")