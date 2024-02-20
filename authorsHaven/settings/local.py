from .base import * #noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Q0OaFWORjmqJzsHckWu5g6iTi_AA-Jv2-3_V2sL_n0qIPaF59QE'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = env("EMAIL_HOST",default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = 'paarasarora2@gmail.com' 
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"




# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False