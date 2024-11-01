from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)

    with app.app_context():
        from .routes import professor_routes
        from .routes import aluno_routes
        from .routes import turma_routes
        app.register_blueprint(professor_routes.bp)
        app.register_blueprint(aluno_routes.bp)
        app.register_blueprint(turma_routes.bp)
        db.create_all()

    return app
