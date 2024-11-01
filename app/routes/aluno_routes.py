from flask import Blueprint, jsonify, request, render_template
from .. import db
from ..models.models import Aluno
from datetime import datetime

bp = Blueprint('aluno_routes', __name__, url_prefix='/alunos')

@bp.route('/', methods=['GET'])
def show_form():
    return render_template('cadastro_aluno.html')

@bp.route('/', methods=['POST'])
def ad_aluno():
    data = request.get_json()
    data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
    novo_aluno = Aluno(
        name=data['name'],
        age=data['age'],
        data_nascimento=data_nascimento,
        nota_primeiro_bimestre=data['nota_primeiro_bimestre'],
        nota_segundo_bimestre=data['nota_segundo_bimestre'],
        media_final=data['media_final'],
        turma_id=data['turma_id']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201
