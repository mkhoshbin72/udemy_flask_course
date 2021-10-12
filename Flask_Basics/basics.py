from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Wolrd!</h1>'

@app.route('/information')
def info():
    return '<h1>People are dumb!</h1>'

@app.route('/people/<name>')
def people(name):
    return '<h1>Hello {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run()