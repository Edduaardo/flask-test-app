from flask import Flask, render_template
from types import SimpleNamespace

#create flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='this is a test from python file')

@app.route('/consultar')
def consultar():
    users = [SimpleNamespace(id=1, firstname='aa', lastname='aab', handle='@abc123'),
        SimpleNamespace(id=2, firstname='bb', lastname='aac', handle='@dfg456')]
    return render_template('consultar.html', users=users)

if __name__ == "__main__":
    app.run(debug=False)
