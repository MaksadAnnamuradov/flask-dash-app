from datetime import timedelta
import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#    python -c "import os; print(repr(os.urandom(24)));"
SECRET_KEY = 'DO_NOT_use_Unsecure_Secrets_in_production_environments'
COOKIE_SECURE = 'Secure'
COOKIE_DURATION = timedelta(days=365)

# MongoDB Config
MONGODB_DB = "mongo"
MONGODB_HOST = 'mongodb+srv://dash:Dash1234@cluster0.jipdo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#MONGODB_PORT = 27017

# Flask Security
SECURITY_PASSWORD_SALT = 'DO_NOT_use_Unsecure_Secrets_in_production'
SECURITY_REGISTERABLE = True
SECURITY_POST_LOGIN_VIEW = 'members.member_page'
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True


# i18n
BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'translations/')

BABEL_DEFAULT_LOCALE = 'en_US'

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps"
# to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps
# (near the bottom).


MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT = 2525
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'd6d92e530b4a3b'
MAIL_PASSWORD = '409f126ee39a44'
MAIL_DEFAULT_SENDER = '"MyApp" <noreply@data-gurus.com>'

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
]
