from flask import Blueprint, jsonify, request, render_template
from .. import db
from ..models.models import Professor

bp = Blueprint('professor_routes', __name__, url_prefix='/professores')

@bp.route('/', methods=['GET'])
def show_form():
    return render_template('cadastro_professor.html')

@bp.route('/', methods=['POST'])
def add_professor():
    data = request.get_json()
    novo_professor = Professor(
        name=data['name'],
        age=data['age'],
        materia=data['materia'],
        observacoes=data['observacoes'],
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify(novo_professor.to_dict()), 201

@bp.route('/list', methods=['GET'])
def list_professores():
    professores = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professores])
