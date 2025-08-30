from config.config import app, db
from flask_cors import CORS
from Routes.viagens import viagem_blueprint
from Model.cargo import Cargo
from Model.area import Area
from Model.gestor import Gestor
from Model.colaborador import Colaborador
from Model.viagem import Viagem
from Model.seed import seed_all

# CORS(app, origins=["http://localhost:5173"]) 


app.register_blueprint(viagem_blueprint)

with app.app_context():
    db.create_all()
    seed_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])