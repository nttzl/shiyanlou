from flask import Blueprint,render_template,abort
from simpledu.models import User,Course

user = Blueprint('user',__name__,url_prefix='/users')

@user.route('/<username>')
def index(username):
    user = User.query.filter_by(username=username).first()
#    courses = Course.query.filter_by(author_id=user.id).all()
    if user:
        return render_template('user/detail.html',user=user)
    else:
        abort(404)
