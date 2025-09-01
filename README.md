

# Matec <img src="static/images/logo_matec.png" alt="Logo Matec" width="40" style="vertical-align: middle; margin-right: 10px;">

Matec é uma plataforma web de aprendizado de matemática voltada para estudantes do IFRN. O objetivo é fornecer conteúdos direcionados, exercícios práticos e suporte personalizado para ajudar alunos a se prepararem para o exame de seleção.

## Funcionalidades

- Cadastro e login de usuários com autenticação segura
- Painel personalizado para cada usuário
- Conteúdos organizados por tópicos de matemática
- Exercícios práticos e material didático
- Comunidade para suporte e troca de conhecimentos
- Interface responsiva e moderna

## Tecnologias Utilizadas

- Python 3
- Flask (framework web)
- Flask-Login (autenticação)
- SQLAlchemy (ORM)
- HTML5, CSS3 (incluindo Bootstrap e Google Fonts)
- JavaScript (quando necessário)

## Estrutura do Projeto

```
Matec/
│
├── app.py                # Arquivo principal da aplicação Flask
├── db.py                 # Configuração do banco de dados
├── models.py             # Modelos de dados (ORM)
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
│
├── instance/             # Configurações e arquivos privados (ex: banco de dados local)
│
├── static/
│   ├── css/              # Arquivos de estilo
│   ├── images/           # Imagens do site
│   └── js/               # Scripts JavaScript
│
├── templates/
│   ├── base.html         # Template base principal
│   ├── base2.html        # Template base alternativo
│   ├── cadastro.html     # Página de cadastro
│   ├── login.html        # Página de login
│   ├── painel.html       # Painel do usuário
│   ├── conteudos.html    # Página de conteúdos
│   ├── sobre.html        # Página sobre
│   ├── index.html        # Página inicial
│   ├── components/       # Componentes reutilizáveis
│   ├── contents/         # Conteúdos específicos
│   └── partials/         # Navbar, footer, etc.
```

## Casos de Uso

- **Cadastro de Usuário:** O estudante acessa a página de cadastro, preenche seus dados e cria uma conta.
- **Login:** O usuário faz login com e-mail e senha para acessar seu painel personalizado.
- **Acesso a Conteúdos:** O usuário navega pelos tópicos de matemática e acessa materiais de estudo.
- **Resolução de Exercícios:** O estudante resolve exercícios práticos e recebe feedback imediato.
- **Participação na Comunidade:** O usuário pode interagir com outros estudantes, tirar dúvidas e compartilhar conhecimento.
- **Gerenciamento de Perfil:** O usuário pode atualizar suas informações pessoais e acompanhar seu progresso.

## Como rodar o projeto

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/Matec.git
   cd Matec
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   # Ative no Windows:
   venv\Scripts\activate
   # Ou no Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```sh
   python app.py
   ```

5. **Acesse no navegador:**
   ```
   http://127.0.0.1:5000/
   ```

## Observações

- O banco de dados e configurações sensíveis ficam na pasta `instance/`, conforme padrão Flask.
- Para adicionar novos conteúdos ou exercícios, edite os arquivos em `templates/contents/` ou `templates/conteudos.html`.

## Licença

Este projeto é apenas para fins educacionais.
<div align="center">
  <img src="static/images/mateco_sentado.png" alt="Logo Matec" width="100" style="vertical-align: middle; margin-right: 10px;">
</div>

---
