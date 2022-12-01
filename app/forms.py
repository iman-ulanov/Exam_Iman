import wtforms as ws
from flask_login import current_user
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[
        ws.validators.DataRequired(), ws.validators.Length(min=4, max=20)])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(), ws.validators.Length(min=8, max=24)])
    submit = ws.SubmitField('Сохранить')


class EmployeeForm(FlaskForm):
    fullname = ws.StringField('ФИО', validators=[ws.validators.DataRequired()])
    phone = ws.StringField('Номер телефона', validators=[ws.validators.DataRequired(), ws.validators.Length(min=13, max=20)])
    short_info = ws.TextAreaField('Краткая информация', validators=[ws.validators.DataRequired()])
    experience = ws.StringField('Опыт работы', validators=[ws.validators.DataRequired()])
    preferred_position = ws.StringField('Желаемая должность')
    user = current_user
    submit = ws.SubmitField('Сохранить')


    def validate_fullname(self, field):
        splitted_fullname = field.data.split(' ')
        if len(splitted_fullname) == 1:
            raise ws.ValidationError('ФИО должно быть полным')
        for name in splitted_fullname:
            if not name.isalpha():
                raise ws.ValidationError('ФИО не может содержать спец.символов и цифр')

    def validate_phone(self, field):
        if field.data[0] != '+':
            raise ws.ValidationError('введите номер через код страны. Например(Кыргызстан: +996)')
