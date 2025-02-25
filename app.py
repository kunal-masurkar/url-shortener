from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random, string

app = Flask(__name__)

# SQLite Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shortener.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

# Generate a short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))

# Route for Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["original_url"]

        # Check if URL already exists
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return render_template("index.html", short_url=request.host_url + existing_url.short_url)

        # Create a new short URL
        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        return render_template("index.html", short_url=request.host_url + short_url)

    return render_template("index.html", short_url=None)

# Route to Redirect Short URL
@app.route("/<short_url>")
def redirect_url(short_url):
    url_entry = URL.query.filter_by(short_url=short_url).first()
    if url_entry:
        return redirect(url_entry.original_url)
    return "URL not found!", 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if not exist
    app.run(debug=True)