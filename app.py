from config.config import app, db
from flask_cors import CORS

CORS(app, origins=["http://localhost:5173"]) 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])