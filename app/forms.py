from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length



class LoginForm(Form):
    openid = TextField('openid', validators=[InputRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(Form):
    nickname = TextField('nickname', validators=[InputRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

