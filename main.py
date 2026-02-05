from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

    def validate_email(self, email):
        if "@" not in email.data or "." not in email.data:
            raise ValidationError("Nao tem gocciola.")
        

    def validate_password(self, password):
        if len(password.data) < 8:
            raise ValidationError("Senha muito curta.")


app = Flask(__name__)
app.secret_key = '12345'


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
