from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/report')
def report():

    username = request.args.get('username')

    # if (any(letter.isupper()) for letter in username):
    #     if (any(letter.islower()) for letter in username):
    #         if username[-1].isdigit():

    return render_template('report.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)