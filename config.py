"""
Configuration for our Flask app.

We NEVER hard-code secret values (like API keys or the secret key)
directly in our code. Instead, we load them from a ".env" file using
python-dotenv. This keeps secrets out of our source code and out of
GitHub.
"""

import os
from dotenv import load_dotenv

# This line reads the ".env" file in your project folder and loads
# its values into the environment, so os.environ.get() can see them.
load_dotenv()


class Config:
    # SECRET_KEY is used by Flask to secure sessions and cookies.
    # We load it from .env; if it's missing, we fall back to a
    # temporary dev-only value so the app doesn't crash (but you
    # should ALWAYS set a real one in .env before deployment).
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-key")

    # This tells SQLAlchemy where our database file lives.
    # "sqlite:///finance_advisor.db" means: use SQLite, and store the
    # database in a file called finance_advisor.db in this folder.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///finance_advisor.db"
    )

    # This turns off a feature we don't need (event tracking) that
    # just uses extra memory and prints a warning if left on.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # We'll use this in Stage 7 (AI recommendations). Reading it here
    # already means it's ready and organized for later.
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
