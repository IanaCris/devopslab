from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World, this is a test done in the devops lab"

if __name__ == '__main__':
    app.run()