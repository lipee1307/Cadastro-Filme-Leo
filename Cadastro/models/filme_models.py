from db import db                       # DE db IMPORTAR db: importa a instância do SQLAlchemy que gerencia o banco de dados

class Filme(db.Model):                   # Define a classe Carro como um modelo do SQLAlchemy (herda de db.Model)
    __tablename__ = 'filmes'              # Nome da tabela no banco de dados será "carros"

    id = db.Column(db.Integer, primary_key=True)          # Coluna "id": número inteiro, chave primária (identificador único)
    titulo = db.Column(db.String(80), nullable=False)     # Coluna "modelo": texto com limite de 80 caracteres, não pode ser nula
    genero = db.Column(db.String(80), nullable=False)      # Coluna "marca": texto com limite de 80 caracteres, não pode ser nula
    duracao = db.Column(db.Integer(80), nullable=False)           # Coluna "ano": número inteiro, não pode ser nulo
    lancamento = db.Column(db.Integer(80), nullable=False)
    diretor = db.Column(db.String(80), nullable=False)    

    def json(self):                                        # Define o método json() que retorna os dados do carro como dicionário
        return {
            'titulo': self.titulo,    # Retorna o modelo do carro
            'genero': self.genero, ''     # Retorna a marca do carro
            'duracao': self.duracao,           # Retorna o ano do carro
            'lancamento': self.lancamento,
            'diretor': self.diretor
        }
