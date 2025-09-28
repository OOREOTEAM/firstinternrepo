from flask import Blueprint , render_template
from flask_login import login_required, current_user
from flask import *
from .models import Photo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    photos = Photo.query.all()
    print()
    return render_template('index.html', photos=photos)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(main)
    app.run(debug=True)
