#!/usr/bin/env python3
from flask import Flask,render_template,request
import json

app = Flask(__name__)

with open('files/helloshiyanlou.json','r') as f:
    d1 = json.loads(f.read())

print(d1)
@app.route('/')
def index():
    return render_template('index.html')

