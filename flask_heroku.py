#!/usr/bin/env python

from os import environ

class Heroku(object):
    """Heroku configurations for flask."""

    def __init__(self, app):
        self.app = app

        # SQL-Alchemy
        self.app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

        # Sentry
        self.app.config['SENTRY_DSN'] = environ.get('SENTRY_DSN')

        # Exceptional
        self.app.config['EXCEPTIONAL_API_KEY'] = environ.get('EXCEPTIONAL_API_KEY')

