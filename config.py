import os

class Config:
    QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://stella:marlyne96@localhost/myblog'
    SQLALCHEMY_TRECK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://stella:marlyne96@localhost/myblog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://stella:marlyne96@localhost/myblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}