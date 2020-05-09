import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def on():
    return "Ta on!!"

@app.route('/cadastrar/empresa')
def cadastrarempresa():
    return ""

@app.route('/login/empresa')
def loginempresa():
    return ""

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)