from flask import render_template
from app.main import bp
from flask_babel import _


@bp.route('/')
@bp.route('/index', methods=['GET'])
def index():
    user = {'username': 'Jack'}
    posts = [
        {'author': 'Mike', 'body': 'Great to see you!'},
        {'author': 'Leon', 'body': 'Enjoy developing.'}
    ]
    # This path indites the path in app/templates/
    return render_template('index.html', title=_('Front Page'), user=user, posts=posts)
