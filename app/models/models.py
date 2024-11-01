from .. import db

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(255))
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'materia': self.materia,
            'observacoes': self.observacoes,
        }

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_bimestre = db.Column(db.Float, nullable=False)
    nota_segundo_bimestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False, default=0.0)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)

    def calculate_media_final(self):
        self.media_final = (self.nota_primeiro_bimestre + self.nota_segundo_bimestre) / 2

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'data_nascimento': self.data_nascimento.strftime('%d-%m-%Y'),
            'nota_primeiro_bimestre': self.nota_primeiro_bimestre,
            'nota_segundo_bimestre': self.nota_segundo_bimestre,
            'media_final': self.media_final,
            'turma_id': self.turma_id,
        }

class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id,
        }