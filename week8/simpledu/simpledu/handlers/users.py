from flask import Blueprint,render_template
from simpledu.models import User,Course

users = Blueprint('users',__name__,url_prefix='/users')

@app.route('/users/<username>')
def user():
    user = User.query.filter_by(username=username).first()
    courses = Course.query.filter_by(author_id=user.id).all()
    return render_template('users.html',user=user,courses=courses)
