"""
Personal Finance Advisor Bot
Stage 1 - Project Setup

This is the main entry point of our Flask application.
Right now it only does 3 things:
1. Creates the Flask app
2. Connects the app to our SQLite database (via SQLAlchemy)
3. Shows a simple "It works!" homepage

We will add registration, login, income, expenses, budgets, AI
recommendations, dashboard etc. in the stages that follow.
"""

from flask import Flask, render_template
from config import Config
from extensions import db


def create_app():
    """
    This function builds and configures our Flask app.
    Using a function (instead of creating the app directly at the top
    of the file) is a best practice called the "Application Factory
    Pattern". It makes testing and scaling the app easier later.
    """
    app = Flask(__name__)

    # Load all our settings (secret key, database path, etc.)
    # from the Config class in config.py
    app.config.from_object(Config)

    # Connect SQLAlchemy (our database toolkit) to this Flask app
    db.init_app(app)

    # Create the database file and tables (if they don't exist yet)
    with app.app_context():
        db.create_all()

    # A simple homepage route, just to prove everything is working
    @app.route("/")
    def home():
        return render_template("home.html")

    return app


# This block only runs when you execute "python app.py" directly.
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
