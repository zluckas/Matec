from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import User

import datetime


app = Flask(__name__)
app.secret_key = 'uma-chave-secreta-segura'  # Chave usada para proteger sessões e cookies

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db.init_app(app)

login_manager = LoginManager(app)  # Inicializa o Flask-Login no app Flask
login_manager.login_view = 'login'  # Define a rota de login para redirecionar usuários não autenticados

# Classe de usuário que o Flask-Login utiliza para gerenciar sessão
class Usuario(UserMixin):
    def __init__(self, id, nome, senha_hash):
        self.id = id  # ID do usuário, usado internamente pelo Flask-Login
        self.nome = nome  # Nome do usuário (para mostrar, por exemplo)
        self.senha_hash = senha_hash  # Senha armazenada em formato hash (não em texto)

# Função obrigatória para o Flask-Login carregar um usuário a partir do ID salvo no banco
@login_manager.user_loader
def load_user(user_id):
    dados = db.session.query(User).filter_by(id=user_id).first()
    if dados:
        return Usuario(dados.id, dados.username, dados.senha) # Cria objeto usuário
    return None  # Retorna None se usuário não encontrado

@app.route('/')
def index():
    return render_template('index.html')  # Página inicial pública

# Rota protegida, só acessível se o usuário estiver logado
@app.route('/painel')
@login_required
def painel():
    return render_template('painel.html', nome=current_user.nome)  # Passa o nome do usuário logado para o template

# Outra rota protegida
@app.route('/conteudos')
@login_required
def conteudos():
    return render_template('conteudos.html')

# Rotas para páginas de conteúdo
@app.route('/fracao')
@login_required
def fracao():
    return render_template('assutos/fracao.html')

@app.route('/conjuntos')
@login_required
def conjuntos():
    return render_template('assutos/conjuntos.html')

@app.route('/sistema')
@login_required
def sistema():
    return render_template('assutos/sistema.html')

@app.route('/potenciacao')
@login_required
def potenciacao():
    return render_template('assutos/potenciacao.html')

@app.route('/radiciacao')
@login_required
def radiciacao():
    return render_template('assutos/radiciacao.html')

# Rota para a página de comunidade
@app.route('/comunidade')
@login_required
def comunidade():
    return render_template('comunidade.html')

# Rotas para funcionalidades do fórum
@app.route('/forum/discussoes')
@login_required
def forum_discussoes():
    # Por enquanto redireciona para a página da comunidade
    # Futuramente pode ter uma página específica para todas as discussões
    return redirect(url_for('comunidade'))

@app.route('/forum/nova-discussao', methods=['GET', 'POST'])
@login_required
def nova_discussao():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        titulo = request.form.get('titulo')
        conteudo = request.form.get('conteudo')
        
        if categoria and titulo and conteudo:
            # Aqui você pode salvar a discussão no banco de dados
            # Por enquanto, apenas mostra uma mensagem de sucesso
            flash(f'Discussão "{titulo}" criada com sucesso na categoria {categoria}!')
            return redirect(url_for('comunidade'))
        else:
            flash('Por favor, preencha todos os campos obrigatórios.')
    
    return render_template('nova_discussao.html')

@app.route('/sobre')
#@login_required
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para processar o formulário de contato
        # Por exemplo, enviar um e-mail ou salvar no banco de dados
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        
        # Exemplo de feedback para o usuário
        flash('Mensagem enviada com sucesso! Entraremos em contato em breve.')
        return redirect(url_for('contato'))
        
    return render_template('contato.html')

# Rota para cadastro de novos usuários
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Captura os dados do formulário de forma segura
        email = request.form.get('email')
        senha = request.form.get('senha')
        nome = request.form.get('nome')
        username = request.form.get('username')
        data_nascimento = request.form.get('data_nascimento')

        # Verifica se algum campo está vazio
        if not email or not nome or not senha or not data_nascimento or not username:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('cadastro'))

        # Validação da idade mínima (10 anos) e máxima (100 anos)
        try:
            data_nasc = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            hoje = datetime.date.today()
            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
            if idade < 10:
                flash('Você precisa ter pelo menos 10 anos para se cadastrar.')
                return redirect(url_for('cadastro'))
            if idade > 100:
                flash('Você precisa ter no máximo 100 anos para se cadastrar.')
                return redirect(url_for('cadastro'))
        except Exception:
            flash('Data de nascimento inválida.')
            return redirect(url_for('cadastro'))

        dados = db.session.query(User).filter_by(username=username).first()

        # Verifica se usuário já existe
        if dados:
            flash('Usuário já existe! Escolha outro nome.')
            return redirect(url_for('cadastro'))

        # Gera hash seguro da senha
        senha_hash = generate_password_hash(senha)

        # definir o usuário a ser salvo
        new_user = User(nome=nome, username=username, email=email, senha=senha_hash, data_nascimento=data_nasc)
        
        # Salva o usuário no banco 
        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))

    # Define limites de data (client-side): mínimo = hoje - 100 anos, máximo = hoje - 10 anos
    hoje = datetime.date.today()
    try:
        min_date_dt = hoje.replace(year=hoje.year - 100)
    except ValueError:
        # Ajusta para anos bissextos (ex.: 29/02)
        min_date_dt = hoje.replace(month=2, day=28, year=hoje.year - 100)
    try:
        max_date_dt = hoje.replace(year=hoje.year - 10)
    except ValueError:
        max_date_dt = hoje.replace(month=2, day=28, year=hoje.year - 10)

    min_date = min_date_dt.strftime("%Y-%m-%d")
    max_date = max_date_dt.strftime("%Y-%m-%d")

    return render_template('cadastro.html', min_date=min_date, max_date=max_date)  

# Rota para login de usuários
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  # email do usuário do formulário
        senha = request.form.get('senha')      # Senha digitada

        # buscar usuário no banco
        resultado = db.session.query(User).filter_by(email=email).first()

        # Verifica se usuário existe e senha está correta
        if resultado and check_password_hash(resultado.senha, senha):
            user = Usuario(resultado.id, resultado.username, resultado.senha)  # Cria objeto usuário
            login_user(user)  # Realiza o login (cria sessão)
            return redirect(url_for('painel'))

        flash('Usuário ou senha incorretos.')
        return redirect(url_for('login'))

    return render_template('login.html')  # Mostra formulário de login

# Rota para logout do usuário
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Remove sessão do usuário
    return redirect(url_for('login'))  # Redireciona para a página de login

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
