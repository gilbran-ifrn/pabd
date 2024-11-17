# pip install flask
from flask import Flask
from flask import render_template

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
    #1. CONEXÃO
    cnx = conectaBD()
    cursorT = cnx.cursor(dictionary=True)
    cursorQ = cnx.cursor(dictionary=True)

    #2. ESCRITA SQL
    sqlListaTotal = 'SELECT * FROM animal'
    sqlQuantidade = 'SELECT COUNT(*) AS qnt FROM animal'

    #3. TRANSAÇÃO
    cursorT.execute(sqlListaTotal)
    resultadoListaTotal = cursorT.fetchall()

    cursorQ.execute(sqlQuantidade)
    resultadoQuantidade = cursorQ.fetchone()

    #4. FECHAR CONEXÃO
    cursorT.close()
    cursorQ.close()
    cnx.close()

    return render_template('lista.html',
                           lTotal = resultadoListaTotal,
                           lQnt = resultadoQuantidade
                           )
