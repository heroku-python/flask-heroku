#!/usr/bin/env python

import urlparse
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
        if 'MAILGUN_SMTP_SERVER' in environ:
            self.app.config.setdefault('SMTP_SERVER', environ.get('MAILGUN_SMTP_SERVER'))
            self.app.config.setdefault('SMTP_LOGIN', environ.get('MAILGUN_SMTP_LOGIN'))
            self.app.config.setdefault('SMTP_PASSWORD', environ.get('MAILGUN_SMTP_PASSWORD'))
            self.app.config.setdefault('MAIL_SERVER', environ.get('MAILGUN_SMTP_SERVER'))
            self.app.config.setdefault('MAIL_USERNAME', environ.get('MAILGUN_SMTP_LOGIN'))
            self.app.config.setdefault('MAIL_PASSWORD', environ.get('MAILGUN_SMTP_PASSWORD'))
            self.app.config.setdefault('MAIL_USE_TLS', True)
        # SendGrid
        elif 'SENDGRID_USERNAME' in environ:
            self.app.config.setdefault('SMTP_SERVER', 'smtp.sendgrid.net')
            self.app.config.setdefault('SMTP_LOGIN', environ.get('SENDGRID_USERNAME'))
            self.app.config.setdefault('SMTP_PASSWORD', environ.get('SENDGRID_PASSWORD'))
            self.app.config.setdefault('MAIL_SERVER', 'smtp.sendgrid.net')
            self.app.config.setdefault('MAIL_USERNAME', environ.get('SENDGRID_USERNAME'))
            self.app.config.setdefault('MAIL_PASSWORD', environ.get('SENDGRID_PASSWORD'))
            self.app.config.setdefault('MAIL_USE_TLS', True)
        
        # Redis To Go
        redis_url = environ.get('REDISTOGO_URL')
        if redis_url:
            url = urlparse.urlparse(redis_url)
            self.app.config.setdefault('REDIS_HOST', url.hostname)
            self.app.config.setdefault('REDIS_PORT', url.port)
            self.app.config.setdefault('REDIS_PASSWORD', url.password)
            
        # Mongolab
        mongolab_uri = environ.get('MONGOLAB_URI')
        if mongolab_uri:
            url = urlparse.urlparse(mongolab_uri)
            self.app.config.setdefault('MONGODB_USER', url.username)
            self.app.config.setdefault('MONGODB_PASSWORD', url.password)
            self.app.config.setdefault('MONGODB_HOST', url.hostname)
            self.app.config.setdefault('MONGODB_PORT', url.port)
            self.app.config.setdefault('MONGODB_DB', url.path[1:])
            
        # MongoHQ
        mongohq_uri = environ.get('MONGOHQ_URL')
        if mongohq_uri:
            url = urlparse.urlparse(mongohq_uri)
            self.app.config.setdefault('MONGODB_USER', url.username)
            self.app.config.setdefault('MONGODB_PASSWORD', url.password)
            self.app.config.setdefault('MONGODB_HOST', url.hostname)
            self.app.config.setdefault('MONGODB_PORT', url.port)
            self.app.config.setdefault('MONGODB_DB', url.path[1:])

        # Cloudant
        cloudant_uri = environ.get('CLOUDANT_URL')
        if cloudant_uri:
            self.app.config.setdefault('COUCHDB_SERVER', cloudant_uri)
