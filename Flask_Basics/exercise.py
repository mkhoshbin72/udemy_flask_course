from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World! Go to name_lattin to see your lattin name.</h1>"

@app.route('/name_lattin/<name>')
def name_lattin(name):
    
    if name[-1] == 'y':
        return "<h1>Hi {}. Your lattin name is {}</h1>".format(name, name.replace(name[-1], 'iful'))

    else:
        return "<h1>Hi {}. Your lattin name is {}</h1>".format(name, name + 'y')

if __name__ == '__main__':
    app.run(debug=True)