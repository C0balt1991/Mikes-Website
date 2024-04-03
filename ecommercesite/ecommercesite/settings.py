"""
Django settings for ecommercesite project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iilw&)986#=ot3xgpgey=!=%g1=5prk1#pnlz3ta=t!*$saz%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store', #DJANGO APP

    'cart', #CART APP

    'account', #ACCOUNT APP

    'payment', #PAYMENT APP

    'mathfilters', #DJANGO MATH APP

    'crispy_forms', #CRISPY APP

    "crispy_bootstrap4",

    'storages', #STORAGE APP

]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommercesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.views.categories', # Updated
                'cart.context_processors.cart',

            ],
        },
    },
]

WSGI_APPLICATION = 'ecommercesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']


MEDIA_URL = '/media/'


MEDIA_ROOT = BASE_DIR / 'static/media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email verification settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Be sure to read the guide in the resource folder of this lecture(SETUP THE EMAIL BACKEND)

EMAIL_HOST_USER = 'businesspurpose984@gmail.com' # - Enter your GMAIL address
EMAIL_HOST_PASSWORD = 'imqtiegjxmlhqtso' # - Enter your app password


# AWS Credentials:

AWS_ACCESS_KEY_ID = "AKIAR3FRZ4EJ5J37PR76"
AWS_SECRET_ACCESS_KEY = "tRug3M/D58ZRI2s0HhGd8XseC+MMlv2fN+HV5Lsv"

# S3 configuration settings:

AWS_STORAGE_BUCKET_NAME = 'mikesfirstbucket1991'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False



# Admin styling adjustment

ADMIN_MEDIA_PREFIX = '/static/admin/'


# RDS (Database) configuration settings:

DATABASES = {

    'default': {
    # Original database, not keeping for any reason

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'demo_1',
        # 'USER': 'Rick',
        # 'PASSWORD': 'Fib11235',
        # 'HOST': 'database-1.cycv0goqnru2.us-east-2.rds.amazonaws.com',
        # 'PORT': '5432',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        
    }

}

SECRET_KEY = env('SECRET_KEY')



# Allow PayPal Popups 

SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'

