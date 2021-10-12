from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')

    return render_template('thankyou.html', firstname=firstname, lastname=lastname)


if __name__ == '__main__':
    app.run(debug=True)