# =============================================================================
# MATEC - Configuração do Banco de Dados
# Inicialização do SQLAlchemy para gerenciamento do banco
# =============================================================================

from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy para ser usada em toda a aplicação
db = SQLAlchemy()