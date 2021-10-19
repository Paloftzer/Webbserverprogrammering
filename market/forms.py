# This calls the necessary packages for our forms to work properly.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email

# This is the code needed to create our registration on our forms.
class RegisterForm(FlaskForm):
    username = StringField(label="User Name: ", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address: ", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password: ", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")