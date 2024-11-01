from flask import Blueprint, jsonify, request, render_template
from .. import db
from ..models.models import Turma, Professor, Aluno

bp = Blueprint('turma_routes', __name__, url_prefix='/turmas')

@bp.route('/', methods=['GET'])
def show_form():
    return render_template('cadastro_turma.html')

@bp.route('/', methods=['POST'])
def add_turma():
    data = request.get_json()
    nova_turma = Turma(
        descricao=data['descricao'], 
        professor_id=data['professor_id'], 
        ativo=data.get('ativo', True),
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify(nova_turma.to_dict()), 201

@bp.route('/list', methods=['GET'])
def list_turmas():
    turmas = Turma.query.all()
    turmas_com_professores = []
    for turma in turmas:
        professor = Professor.query.get(turma.professor_id)
        turma_dict = turma.to_dict()
        turma_dict['professor_name'] = professor.name if professor else 'N/A'
        turmas_com_professores.append(turma_dict)
    return jsonify(turmas_com_professores)

@bp.route('/<int:turma_id>/alunos', methods=['GET'])
def list_alunos(turma_id):
    alunos = Aluno.query.filter_by(turma_id=turma_id).all()
    alunos_list = [aluno.to_dict() for aluno in alunos]
    return jsonify(alunos_list)