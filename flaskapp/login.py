
from flask.ext.login import LoginManager
from flask.ext.login import login_user
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import AnonymousUserMixin
from flaskapp import flasktemplate

class Anonymous(AnonymousUserMixin):

    def __init__(self):
        self.username = 'Guest'
        self.name = 'Guest'


login_manager = LoginManager()
login_manager.init_app(flasktemplate)
login_manager.login_view = '{app}.login'.format(app=appnamed)
login_manager.login_message = 'Please log in.'
login_manager.anonymous_user = Anonymous


@login_manager.user_loader
def load_user(user_id):
    """Hook for Flask-Login to load a User instance from a user ID."""
    return session.query(User).get(user_id)


login_manager.anonymous_user = Anonymous
