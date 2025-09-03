import os

# define base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# baseline configuration
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATION = False

    # static method for initialization
    @staticmethod
    def init_app(app):
        pass


# define class that subclasses from the regular configuration
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "prod.sqlite")


# define dictionary for this configuration that we are referencing before
env_config = {
    "production": ProductionConfig,
}
