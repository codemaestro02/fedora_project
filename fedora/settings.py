"""
Django settings for fedora project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
# from dotenv import Dotenv
from dotenv import main

import os

import re

main.load_dotenv()
# env = Dotenv('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# with open('./secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    'main',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',
    'ckeditor', 
    'ckeditor_uploader',
    'taggit',
    'author',
    'programs',
    'career',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'author.middlewares.AuthorDefaultBackendMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'fedora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fedora.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'URL': os.getenv('DATABASE_URL'),
        'NAME': os.getenv('DBNAME'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPASSWORD'),
        'HOST': os.getenv('DBHOST'),
        'PORT': os.getenv('DBPORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = 'static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#Add this in your settings.py file:
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


IGNORABLE_404_URLS = [
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        },
        'APP': {
            'client_id': '573351541202-i8qnfn9n8hbugmj7iglte0j9ai3df73o.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'OAUTH_PKCE_ENABLED': True,

    }
}


ACCOUNT_FORMS = {
    'signup': 'users.signupform.MyCustomSignupForm',
    'login':'allauth.account.forms.LoginForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',   
}

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_SESSION_REMEMBER = "None"
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Site]"
ACCOUNT_ADAPTER = 'users.adapter.MyAccountAdapter'
ACCOUNT_USERNAME_VALIDATORS = 'users.validators.custom_username_validators'

SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL= '/accounts/login/'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend'
]

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_RESTRICT_BY_DATE = True

CKEDITOR_IMAGE_BACKEND = 'ckeditor_uploader.backends.Pillow'

CKEDITOR_FORCE_JPEG_COMPRESSION = True

CKEDITOR_IMAGE_QUALITY = 90

CKEDITOR_ALLOW_NONIMAGE_FILES = False


TAGGIT_CASE_INSENSITIVE = True

AUTHOR_CREATED_BY_FIELD_NAME = "author"
AUTHOR_UPDATED_BY_FIELD_NAME = "updated"

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


