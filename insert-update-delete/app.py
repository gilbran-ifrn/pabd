# pip install flask
from flask import Flask
from flask import render_template
from flask import request

# pip install mysql-connector-python
#import mysql.connector
from mysql.connector import (connection)

app = Flask(__name__)

# Função retorna a conexão do banco
def conectaBD():
    #cnx = mysql.connector.connect(
    cnx = connection.MySQLConnection(
        user='root',
        password='senharoot',
        host='127.0.0.1',
        database='petshop')
    
    return cnx


@app.route('/')
def index():
    return render_template('forms.html')

@app.route('/insercao', methods=['POST'])
def inserir():
    #1. CONEXÃO
    cnx = conectaBD()
    cursor = cnx.cursor()

    #2. ESCRITA SQL
    sql = 'INSERT INTO animal (nome, raca) VALUES (%s, %s)'
    dados = (request.form['nome'], request.form['raca'])

    #3. TRANSAÇÃO
    cursor.execute(sql, dados)
    cnx.commit()

    #4. FECHAR CONEXÃO
    cursor.close()
    cnx.close()

    return 'INSERÇÃO CONCLUÍDA'

@app.route('/atualizacao', methods=['POST'])
def atualizar():
    #1. CONEXÃO
    cnx = conectaBD()
    cursor = cnx.cursor()

    #2. ESCRITA SQL
    sql = 'UPDATE animal SET nome=%s, raca=%s WHERE id=%s'
    dados = (request.form['nome'], request.form['raca'], request.form['id'])

    #3. TRANSAÇÃO
    cursor.execute(sql, dados)
    cnx.commit()

    #4. FECHAR CONEXÃO
    cursor.close()
    cnx.close()

    return 'ATUALIZAÇÃO CONCLUÍDA'

@app.route('/remocao', methods=['POST'])
def remover():
    #1. CONEXÃO
    cnx = conectaBD()
    cursor = cnx.cursor()

    #2. ESCRITA SQL
    sql = 'DELETE FROM animal WHERE id=%s'
    dados = (request.form['id'],) # a vírgula é deixada aqui para garantir que o dado é uma tupla

    #3. TRANSAÇÃO
    cursor.execute(sql, dados)
    cnx.commit()

    #4. FECHAR CONEXÃO
    cursor.close()
    cnx.close()

    return 'REMOÇÃO CONCLUÍDA'