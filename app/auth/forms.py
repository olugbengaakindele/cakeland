from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, ValidationError, InputRequired, EqualTo
from wtforms.fields.html5 import EmailField

'''
def check_email(form, field):
        if '*@*.*' in field.data:
            raise ValidationError(
                'email already exist, please go to login page')

'''

class ContactUs(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [InputRequired(),
    Email(message="please enter a valid email format")])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

class PictureUpload(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format")])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class NewUserForm(FlaskForm):
    username = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format")])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')