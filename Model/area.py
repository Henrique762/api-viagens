from config.config import db


class Area(db.Model):
    __tablename__ = "area"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    area = db.Column(db.String(255), nullable=False)

def data_area():
    status_list = ['financeiro', 'recursos humanos', 'comercial', 'marketing', 'suporte', 'ti', 'operacoes', 'logistica']
    if Area.query.first():
        print("Areas já cadastradas.")
        return

    for nome in status_list:
        status = Area(nome=nome)
        db.session.add(status)
    
    db.session.commit()
    print("Areas inseridas com sucesso!")