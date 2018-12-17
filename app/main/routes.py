from flask import render_template, url_for
from app.main import bp
from flask import current_app


@bp.route('/')
@bp.route('/index', methods=['GET'])
def index():
    user = {'username': 'Jack'}
    posts = [
        {'author': 'Mike', 'body': 'Great to see you!'},
        {'author': 'Leon', 'body': 'Enjoy developing.'}
    ]
    # This path indites the path in app/templates/
    return render_template('index.html', user=user, posts=posts)
