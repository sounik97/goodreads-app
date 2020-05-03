import os

from flask import Flask, session, redirect, url_for
from flask_session import Session
from sqlalchemy_utils import database_exists, create_database, drop_database

from blueprints.user_blueprint import user_blueprint
from blueprints.book_blueprint import book_blueprint
from init_db import create_all_tables


from db import db


app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(book_blueprint)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
    # raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))


#redirecing to user_blueprint as entry page
@app.route("/")
def index():
    return redirect(url_for('user_blueprint.register'))


if __name__ == "__main__":
    app.run(debug=True)
