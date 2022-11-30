from flask_wtf import FlaskForm
import wtforms as ws

class TransactionsForm(FlaskForm):
    period = ws.StringField('Наименование перевода', validators=[ws.validators.DataRequired(), ])
    value = ws.IntegerField('Сумма', validators=[ws.validators.DataRequired(), ])
    status = ws.StringField('Статус')
    unit = ws.SelectField('Валюта',choices=(("kgs"),("rub"),("usd"),("eur"),("kzt"),("cny"),("gbp")))
    subject = ws.TextAreaField('Коментарии')

class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[ws.validators.DataRequired(), ws.validators.Length(min=4,max=20)])
    password = ws.PasswordField('Пароль', validators=[ws.validators.DataRequired(), ws.validators.Length(min=8, max=24)])