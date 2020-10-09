from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


##the base configuration
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True ## CSRF (Cross Site Request Forgery)
    SECRET_KEY = environ.get('SECRET_KEY')

##the config for production environment
class ProductionConfig(Config):
    DEBUG = False

##the config for stage environment
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

##the config for development environment
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

##the config for testing environment
class TestingConfig(Config):
    TESTING = True



'''
Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute
unwanted actions on a web application in which they’re currently authenticated.
With a little help of social engineering (such as sending a link via email or chat),
an attacker may trick the users of a web application into executing
actions of the attacker’s choosing. If the victim is a normal user,
a successful CSRF attack can force the user to perform state changing requests like
transferring funds, changing their email address, and so forth.
If the victim is an administrative account, CSRF can compromise the entire web application.
'''
