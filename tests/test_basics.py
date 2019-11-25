# -*- coding: utf-8 -*- 
# @Time : 2019/11/25 9:18 上午 
# @Author : Lian 
# @Site :  
# @File : test_basics.py 
# @Software: PyCharm
import unittest
from flask import current_app
from app import create_app, db


# app_context 的push部分尚有一些疑问
class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
