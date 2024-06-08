from flask import Flask, make_response,jsonify,request
from nomes import nomes #usei outro arquivo .py como bd para aplicar o conhecimneto

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/nomes',methods=['GET'])
def get_nomes():
    return make_response(
        jsonify(nomes)
    )

@app.route('/nomes',methods=['POST'])
def inserir_nome():
    nome = request.json
    nomes.append(nome)
    return make_response(
        jsonify(nome)
    )

app.run()