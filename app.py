from flask import Flask, render_template
from flask import request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/painel')
def painel():
    return render_template('painel.html')

@app.route('/conteudos')
def conteudos():
    return render_template('conteudos.html')