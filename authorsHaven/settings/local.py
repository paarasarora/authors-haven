from .base import * #noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Q0OaFWORjmqJzsHckWu5g6iTi_AA-Jv2-3_V2sL_n0qIPaF59QE'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']