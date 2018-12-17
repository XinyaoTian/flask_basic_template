from flask import render_template, url_for
from app import app


@app.route('/')
@app.route(url_for('index'), methods=['GET'])
def index():
    user = {'username': 'Jack'}
    posts = [
        {'author': 'Mike', 'body': 'Great to see you!'},
        {'author': 'Leon', 'body': 'Enjoy developing.'}
    ]
    return render_template('index.html', user=user, posts=posts)
