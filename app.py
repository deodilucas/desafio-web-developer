from flask import Flask, request, render_template, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

connect = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    database='db_desafio',
)
cur = connect.cursor()

@app.route('/')
def Index():
    sql = 'SELECT id, nome_acao, data_prevista, investimento \
    FROM acao\
    INNER JOIN tipo_acao ON acao.codigo_acao = tipo_acao.codigo_acao;'
    cur.execute(sql)
    action = cur.fetchall()
    return render_template('index.html', action=action)

@app.route('/inserir', methods = ['POST'])
def cad():
    acao = request.form['acao']
    date_exp = request.form['date_exp']
    invest_exp = request.form['invest_exp']
    date_now = datetime.now().date()
    cur.execute('INSERT INTO acao (codigo_acao, investimento, data_prevista, data_cadastro) VALUES (%s, %s, %s, %s)', (acao,invest_exp,date_exp,date_now))
    connect.commit()
    return redirect('/')
    
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cur.execute('DELETE FROM acao WHERE id=%s',(id_data,))
    connect.commit()
    return redirect('/')

@app.route('/update/<string:id_data>', methods = ['POST','GET'])
def update(id_data):
    acao = request.form['acao']
    date_exp = request.form['date_exp']
    invest_exp = request.form['invest_exp']
    cur.execute('UPDATE acao SET codigo_acao=%s, data_prevista=%s, investimento=%s WHERE id=%s',(acao, date_exp, invest_exp, id_data))
    connect.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)