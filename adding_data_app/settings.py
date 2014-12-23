"""
Django settings for adding_data_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x&@p5fe1ep&)d)339z=4-ki96p91o9uofseei!+rq$s6t96l$#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #PART 6.2 this part here is where you are going to add the apps in the project!!! This would be where within the Google app you tell the project, hey, big Google app, here are the little apps you are going to work on. Here is the calendar, and maps, and gmail, etc.  In the line below, we are going to add the app folder. 
    'app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adding_data_app.urls'

WSGI_APPLICATION = 'adding_data_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        #PART 6.3 you are also changing the stuff below because we are creating a new database for this parent app >> the BIG Google and we have to tell the children apps where they are supposed to go'

        #Before you do this step, log into the http://127.0.0.1:8000/admin/ using your username and password... if you don't know your username and password... use the following site to reset >>http://stackoverflow.com/questions/6358030/how-to-reset-django-admin-password<< or google 'create new superuser django' and follow the prompt

        #After you have finally logged into the django admin site, go in your local drive to the folder that has manage.py from your terminal and type $python manage.py syncdb  This is going to allow the DB to sync with what we have put in settings and in the models. 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adding_data_app',
        'USER': 'postgres',
        'PASSWORD': 'newpassword',
        'HOST': 'localhost',
        'PORT':'',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
