from .base import *


DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memories',
        'USER': 'oliver',
        'PASSWORD': 'yugiho2000',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
MEDIA_URL = '/media/'
STATICFILES_DIRS=[
	os.path.join(os.path.dirname(BASE_DIR),'static'),
		]



