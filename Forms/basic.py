from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, BooleanField, IntegerField
from wtforms.validators import  DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

class InfoForm(FlaskForm):

    name = StringField('What is your name?')#, validators=[DataRequired()])
    # age = IntegerField('How old are you?')
    # gender = RadioField('Choose your gender:', choices=[('male', 'Male'), ('female', 'Female')])
    # married = BooleanField('Are you married?')
    # info = TextAreaField('Any other info?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():

        name = form.name.data
        # session['age'] = form.age.data
        # session['gender'] = form.gender.data
        # session['married'] = form.married.data
        # session['info'] = form.info.data
        # session['submit'] = form.submit.data

        flash(f"Thank tou for submiting {name}")

        return redirect(url_for('index'))


    return render_template('index.html', form=form)


# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)