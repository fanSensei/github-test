#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019\2\26 0026 10:38
# @Author  : luf
# from flask import Flask, abort, redirect, url_for, render_template
#
# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
#
# @app.route('/')
# def hello():
#     return render_template('login.html')
#
#
# @app.route('/login')
# def login():
#     abort(401)
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('login.html'), 404

from flaskr import create_app
if __name__ == '__main__':
    create_app().run()
