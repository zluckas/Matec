# =============================================================================
# MATEC - Modelos de Banco de Dados
# Definições das tabelas e relacionamentos do sistema
# =============================================================================

from db import db

class User(db.Model):
    """Modelo de usuário do sistema"""
    __tablename__ = 'usuarios'
    
    # Campos da tabela
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    nome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(250), nullable=False)  # Hash da senha
    data_nascimento = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'
