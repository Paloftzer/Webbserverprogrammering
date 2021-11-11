# forms.py file

#* This calls the necessary packages for our form to work properly.
from flask_wtf import FlaskForm # This imports the FlaskForm from our flask_wtf library.
from wtforms import StringField, PasswordField, SubmitField # This imports the different types of fields that we use on our form.
from wtforms.validators import Length, DataRequired, EqualTo, Email # This imports the validators that we use in our form to make sure that the user inputs the correct data.

#* This is the code needed to create our registration on our forms.
#* This defines that it is form created with FlaskForm.
class RegisterForm(FlaskForm):
    #* Length is the length that the submitted data must have, DataRequired means that something must have been entered in that field, and EqualTo means that the entered data must be equal to the data entered in the field that the validator checks.
    # This creates the StringField (text field) where the user inputs the username they desire for their account, because of the validators it needs to be between 2 and 30 characters long, and data must be entered otherwise an error occurs.
    username = StringField(label="User Name: ", validators=[Length(min=2, max=30), DataRequired()])
    # This creates the StringField (text field) where the user inputs their email address, and because of the validators it needs to be a valid email, and data must be entered.
    email_address = StringField(label="Email Address: ", validators=[Email(), DataRequired()])
    # This creates the PasswordField (a field which hides the data that was entered with asterisks) where the user inputs their desired password, and because of the validators it needs to have a minimum length of 6 characters and as before, data must be entered.
    password1 = PasswordField(label="Password: ", validators=[Length(min=6), DataRequired()])
    # This creates the PasswordField (a field which hides the data that was entered with asterisks) where the user must re enter their password, and because of the validators it needs to be the same as the previous password, and data must be entered.
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo("password1"), DataRequired()])
    # This creates a SubmitField that when clicked will send (POST) the data to the database.
    submit = SubmitField(label="Create Account")