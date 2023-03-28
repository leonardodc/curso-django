from .settings import *
import os

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []


# hostname = os.environ['DBHOST']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DBNAME'],
#         'HOST': hostname + ".postgres.database.azure.com",
#         'USER': os.environ['DBUSER'],
#         'PASSWORD': os.environ['DBPASS'] 
#     }
# }

# https://learn.microsoft.com/pt-br/training/modules/django-deployment/4-prepare-for-deployment

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False