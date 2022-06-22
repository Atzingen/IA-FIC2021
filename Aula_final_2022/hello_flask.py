from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    nome = 'Gustavo'
    numeros = [i for i in range(21)]
    return render_template('hello.html', 
                            nome=nome, numeros=numeros)

@app.route('/user/<user_name>')
def get_user(user_name):
    return f'<h1> Hello {user_name} ! </h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)