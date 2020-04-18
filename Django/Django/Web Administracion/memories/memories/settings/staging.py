from .base import *

DEBUG = False
ALLOWED_HOSTS = ['memoriespets.herokuapp.com','.memoriespets.com']
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcohh21fuvb45n',
        'USER': 'pcoxbrarqcyrgi',
        'PASSWORD': '5584dd371d841e2a080edbf7947a269e959ac3030e1ca120ac2635df1c053fe3',
        'HOST': 'ec2-54-221-251-195.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
STATICFILES_DIRS=[
	os.path.join(os.path.dirname(BASE_DIR),'static'),
		]
