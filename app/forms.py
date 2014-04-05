from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import InputRequired



class LoginForm(Form):
    openid = TextField('openid', validators=[InputRequired()])
    remember_me = BooleanField('remember_me', default=False)
