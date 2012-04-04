#!/usr/bin/env python

from os import environ

class Heroku(object):
    """Heroku configurations for flask."""

    def __init__(self, app):
        self.app = app

        # SQL-Alchemy
        self.app.config.setdefault('SQLALCHEMY_DATABASE_URI', environ.get('DATABASE_URL'))

        # Sentry
        self.app.config.setdefault('SENTRY_DSN', environ.get('SENTRY_DSN'))

        # Exceptional
        self.app.config.setdefault('EXCEPTIONAL_API_KEY', environ.get('EXCEPTIONAL_API_KEY'))

        # Flask-GoogleFed
        self.app.config.setdefault('GOOGLE_DOMAIN', environ.get('GOOGLE_DOMAIN'))

        # Celery w/ RabbitMQ
        self.app.config.setdefault('BROKER_URL', environ.get('RABBITMQ_URL'))

        # Mailgun
        self.app.config.setdefault('SMTP_SERVER', environ.get('MAILGUN_SMTP_SERVER'))
        self.app.config.setdefault('SMTP_LOGIN', environ.get('MAILGUN_SMTP_LOGIN'))
        self.app.config.setdefault('SMTP_PASSWORD', environ.get('MAILGUN_SMTP_PASSWORD'))