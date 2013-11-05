"""
Flask-Heroku
------------

This is a super simple Flask extension that provides some app configuration
defaults based on the Heroku-esque environment variables.
"""

from setuptools import setup


setup(
    name='flask-heroku',
    version='0.1.3',
    url='https://github.com/kennethreitz/flask-heroku',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Heroku environment variable configurations for Flask',
    long_description=__doc__,
    py_modules=['flask_heroku'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
