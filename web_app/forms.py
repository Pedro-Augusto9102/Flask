from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegistroForm(FlaskForm):
    name = StringField(label='Usuario', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    senha = PasswordField(label='Senha', validators=[Length(min=6), DataRequired()])
    conf_senha = PasswordField(label='Confirma senha', validators=[EqualTo('senha'), DataRequired()])
    cadastrar = SubmitField(label='Cadastrar')
    
class RegistroInfo(FlaskForm):
    marca = StringField(label='Marca', validators=[Length(min=2, max=30), DataRequired()])
    desc = StringField(label='Desc', validators=[DataRequired()])
    img = PasswordField(label='IMG', validators=[Length(min=6)])
    cadastrar1 = SubmitField(label='Cadastrar')