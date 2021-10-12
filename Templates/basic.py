from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'mohammad'
    letters = list(name)
    name_dict = {'name':'mohammad'}
    return render_template('basic.html', name=name, letters=letters, name_dict=name_dict)


if __name__ == '__main__':
    app.run(debug=True)