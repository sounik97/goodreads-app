import os

from flask import Flask, session, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from blueprints.user_blueprint import user_blueprint
from init_db import create_all_tables


app = Flask(__name__)

app.register_blueprint(user_blueprint)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
    # raise RuntimeError("DATABASE_URL is not set")

DATABASE_URL = 'postgres://vtxfxgdjyhapnc:6c42ff36dc32ef50a4e33bde584964bd9735a0284addefaec38b2f724b844485@ec2-34-225-82-212.compute-1.amazonaws.com:5432/dadhl1lseoo0fe'

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))


#redirecing to user_blueprint as entry page
@app.route("/")
def index():
    return redirect(url_for('user_blueprint.register'))


if __name__ == "__main__":
    app.run(debug=True)
