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


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])


class InvoiceSearchForm(Form):
    customer = StringField('customer', validators=[DataRequired()])
    start_date = StringField('start_date', validators=[DataRequired()])
    end_date = StringField('end_date', validators=[DataRequired()])


class PageDownFormExample(Form):
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')
