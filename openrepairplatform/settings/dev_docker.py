from .base import *  # noqa
import os
import socket
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

ALLOWED_HOSTS += ['localhost', '127.0.0.1', 'django', 'selenium']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "HOST": 'db',
        "PORT": "5432",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    }
}
