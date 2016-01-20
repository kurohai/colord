"""Forms to render HTML input & validate request data."""

from wtforms import BooleanField, DateTimeField, PasswordField
from wtforms import TextAreaField, StringField
from wtforms.validators import Length, DataRequired
from wtforms import validators
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms.fields import SubmitField


class LoginForm(Form):
    """Render HTML input for user login form.
    Authentication (i.e. password verification) happens in the view function.
    """
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])



class ColorForm(Form):
    colors = TextAreaField('colors', validators=[DataRequired()])
