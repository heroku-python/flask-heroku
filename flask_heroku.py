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
        self.app.config.setdefault('SMTP_SERVER', environ.get('MAILGUN_SMTP_SERVER'))
        self.app.config.setdefault('SMTP_LOGIN', environ.get('MAILGUN_SMTP_LOGIN'))
        self.app.config.setdefault('SMTP_PASSWORD', environ.get('MAILGUN_SMTP_PASSWORD'))
        
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

        # Memcachier
        self.app.config.setdefault('MEMCACHED_SERVERS', environ.get('MEMCACHIER_SERVERS'))
        self.app.config.setdefault('MEMCACHED_USERNAME', environ.get('MEMCACHIER_USERNAME'))
        self.app.config.setdefault('MEMCACHED_PASSWORD', environ.get('MEMCACHIER_PASSWORD'))