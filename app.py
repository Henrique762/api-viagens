from config.config import app, db
from flask_cors import CORS
from Routes.viagens import viagem_blueprint
from Routes.aprovacao_viagem import aprovacaoviagem_blueprint
from Routes.colaborador import colaborador_bp
from Routes.auth import auth_bp
from Routes.reserva import reserva_bp
from Routes.gestor import gestor_bp
from Model.cargo import Cargo
from Model.area import Area
from Model.gestor import Gestor
from Model.colaborador import Colaborador
from Model.viagem import Viagem
from Model.seed import seed_all

# CORS(app, origins=["http://localhost:5173"]) 


app.register_blueprint(viagem_blueprint)
app.register_blueprint(aprovacaoviagem_blueprint)
app.register_blueprint(colaborador_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(gestor_bp)

with app.app_context():
    db.create_all()
    seed_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])