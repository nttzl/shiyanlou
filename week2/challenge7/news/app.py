#!/usr/bin/env python3
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/nttzl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref='files')

    content = db.Column(db.Text)
    
    def __init__(self,title,category,content,created_time=None):
        self.title = title
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return '<File %r>' % self.title


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category %r>' % self.name


db.drop_all()
db.create_all()
java = Category('Java')
python = Category('Python')
db.session.add_all([java,python])
db.session.commit()
file1 = File('Hello Java',java,'File Content - Java is cool!')
file2 = File('Hello Python',python,'File Content - Python is cool!')
db.session.add_all([file1,file2])
db.session.commit()
#    app.run(port=3000)

#   print(File.query.all())

@app.route('/')
def index():
    return render_template('index.html',l = File.query.all())

@app.route('/files/<file_id>')
def file(file_id):
    f = File.query.get_or_404(file_id)
    return render_template('file.html',f = f)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

