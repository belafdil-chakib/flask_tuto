from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/predict/<int:id_client>')
def predict(id_client):
    return [id_client, 2*id_client, id_client/5]


if __name__ == '__main__':
    app.run()
