# -*- coding: utf-8 -*- 
# @Time : 2019/11/21 8:20 下午 
# @Author : Lian 
# @Site :  
# @File : __init__.py
# @Software: PyCharm
from flask import Blueprint

# 定义蓝图
main = Blueprint('main', __name__)

# 避免循环引用
from . import views, errors

