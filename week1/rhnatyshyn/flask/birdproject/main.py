from flask import Flask, Blueprint , render_template, request, redirect
from flask_login import login_required, current_user
from .models import Photo, Hunter
import hashlib

main = Blueprint('main', __name__)
@main.before_app_request
def debug():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0]
    ip_hashed =hashlib.sha256(str.encode(ip)).hexdigest()
    hunter_entry = Hunter.query.filter_by(ip_hash=ip_hashed).first()
        
    if hunter_entry:
        return redirect("https://zakon.rada.gov.ua/laws/show/2341-14/paran1668#n1668")

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
