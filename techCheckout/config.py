#Base code taken from https://github.com/Dr-Crow/cmpt-221-examples/tree/master/Examples/example_of_new_layout
#and then altered to match our needs.
import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Creates base config
class Config:
    # Secret Key used for forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # Disable tracking to save on memory and performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Setting up our database variables
    DATABASE_IP = os.environ.get('DATABASE_IP') or "127.0.0.1"
    DATABASE_PORT = os.environ.get('DATABASE_PORT') or "5432"
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME') or "postgres"
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or "Wasdwasd123"
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or ""

    # Allows use to call SQLALCHEMY_DATABASE_URI as if it was set as attribute  in this class
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "postgresql://{username}:{password}@{ip}:{port}/{name}".format(username=self.DATABASE_USERNAME,
                                                                              password=self.DATABASE_PASSWORD,
                                                                              ip=self.DATABASE_IP,
                                                                              port=self.DATABASE_PORT,
                                                                              name=self.DATABASE_NAME)

    @staticmethod
    def init_app(app):
        pass


# For develop config
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or "dev"


# For testing config
class TestingConfig(Config):
    TESTING = True
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or "test"


# For production config
class ProductionConfig(Config):
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or "prod"


# Allows use to pass in a name and get back the right config based on the name
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
