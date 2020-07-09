import sqlite3
from flask import (Flask, render_template, g, flash,\
        request, session, abort, redirect, url_for)

DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def db_conn():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()


