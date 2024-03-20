import sympy as sp
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def formatar_matriz(matriz):
    table = '<table border="1">'
    for linha in matriz:
        table += '<tr>'
        for elemento in linha:
            elemento_simplificado = sp.nsimplify(elemento)
            table += '<td>' + str(elemento_simplificado) + '</td>'
        table += '</tr>'
    table += '</table>'
    return table

@app.route('/', methods=['POST'])
def escalonar_matriz():
    matriz_str = request.form['matriz']
    matriz = [[sp.Rational(num) for num in linha.split()] for linha in matriz_str.split('\n')]
    matriz_sym = sp.Matrix(matriz)
    matriz_escalada_sym, _ = matriz_sym.rref()  # Desempacotando a tupla
    matriz_escalada_formatada = formatar_matriz(matriz_escalada_sym.tolist()) + '<br>'
    return matriz_escalada_formatada

if __name__ == '__main__':
    app.run()
