# -*- coding: utf-8 -*- 
# @Time : 2019/11/21 8:22 下午 
# @Author : Lian 
# @Site :  
# @File : flasky.py
# @Software: PyCharm
# @Note: defines the Flask application instance, and also includes a few tasks that help manage the application
import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role

# 创建flask app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# 初始化migrate，用于数据库的upgrade
migrate = Migrate(app, db)

# 设定shell运行情况下的，自动引入的objects
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# click 设置命令行的参数
@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)