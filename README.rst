Flask-Heroku
============

This is a simple Flask extension that sets configuration defaults for
Heroku-esque environment variables.

This is far from conclusive. Send a pull request to add a new service!


Usage
-----

Usage is pretty simple::

    from flask import Flask
    from flask_heroku import Heroku

    app = Flask(__name__)
    heroku = Heroku(app)

Configuration is already set up::

    >>> app.config['SQLALCHEMY_DATABASE_URI']
    postgres://...

Alternatively, Flask's application factory pattern is supported::

    heroku = Heroku()
    # Then, later...
    heroku.init_app(app)

Install
-------

Installation is simple::

    $ pip install flask-heroku