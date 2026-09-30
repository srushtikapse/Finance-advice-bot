"""
This file just creates the SQLAlchemy database object.

Why a separate file? Because in later stages, our models.py file
(database tables) and our app.py file both need access to the same
"db" object. Putting it here, in its own small file, avoids a
Python problem called a "circular import" (two files trying to
import each other).
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
