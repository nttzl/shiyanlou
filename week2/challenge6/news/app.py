#!/usr/bin/env python3
from flask import Flask,render_template,request
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def read_json(file):
    
    with open(file,'r') as f:
        d = json.loads(f.read())
    return d

d1 = read_json('files/helloshiyanlou.json')
d2 = read_json('files/helloworld.json')

@app.route('/')
def index():
    return render_template('index.html',d1=d1,d2=d2)

@app.route('/files/<filename>')
def file(filename):

    if filename == 'helloshiyanlou':
        result = render_template('file.html',filename=filename,d=d1)
    elif filename == 'helloworld':
        result = render_template('file.html',filename=filename,d=d2)
    else:
        result = render_template('404.html'),404
    return result

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


