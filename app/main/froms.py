# -*- coding: utf-8 -*- 
# @Time : 2019/11/21 8:48 下午 
# @Author : Lian 
# @Site :  
# @File : froms.py 
# @Software: PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
