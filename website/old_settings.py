"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-7n@xxr3c0&_ou+fd$@b4&x4m_q8xl&$v=d2kjule9sffkjl%=&'
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = env("DEBUG",default=False)

ALLOWED_HOSTS = []




# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #######   OTHERS  #########
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
]

CUSTOM_APPS = [
    "accounts.apps.AccountsConfig",
    "parents.apps.ParentsConfig",
    "staffs.apps.StaffsConfig",
    "students.apps.StudentsConfig",
    "student_classes.apps.StudentClassesConfig",
    "pages.apps.PagesConfig",
]

THIRD_PARTY_APPS=[
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    # 'crispy_bootstrap5',
    'easy_thumbnails',
    'debug_toolbar',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.telegram',
    # 'allauth.socialaccount.providers.twitter',
]



INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# CRISPY_TEMPLATE_PACK = 'bootstrap5'


MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',#Cache
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ##########################################################
    'debug_toolbar.middleware.DebugToolbarMiddleware',# Tool bar
    'django.middleware.cache.FetchFromCacheMiddleware',#Cache
]

######CACHE 
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = " "

ROOT_URLCONF = 'website.urls'

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
                'pages.context_processors.all_pages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'






AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}







# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "db",#Set in the docker-compose.yml
#         "PORT": 5432,#Default postgres port
#     }
# }


LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGOUT_REDIRECT_URL = 'pages:home'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_URL = 'account_login'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 500
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'admin1', 'admin2', ]
# DEFAULT_FROM_EMAIL = 'noreply@oakpremier.com'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True



# # ACCOUNT_FORMS = {'login': 'user.forms.MyCustomLoginForm'}
# ACCOUNT_FORMS = {'signup': 'user.forms.MyCustomSignupForm'}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT"),
    }
}


AUTH_USER_MODEL = "accounts.User"



THUMBNAIL_ALIASES = {
    '': {
        'student_image': {'size': (271, 203), 'crop': True},
        'coin_logo': {'size': (50, 50), 'crop': True},

    },
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

######## SENDING EMAIL IN LOCAL DEVELOPMENT
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Specifying to django where to look for the static files
STATICFILES_DIRS = [
    (BASE_DIR / 'website/static')
]

# url to access your static files
STATIC_URL = '/static/'

# where to save the static files to, when we run collectstatics
STATIC_ROOT = (BASE_DIR / 'static')

# Directory where our media files will be saved to
MEDIA_ROOT = (BASE_DIR / 'media')

# Url in which we can access our media files
MEDIA_URL = '/media/'

#Static file storage engine NB:Its already this by default we are just stating it
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"








# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


AUTHOR='Programmer Izak'
SITE_NAME = 'Celebrity International School '
SITE_TAGLINE="Website Development | Mobile Apps | Desktop | Custom Solutions | Digital Services | There's a Solution ... " 
META_KEYWORDS='''website hosting,HTML,CSS,ASP,.NET,JavaScript,SQL,PHP,jQuery,XML,DOM,Bootstrap,Python,
Java,Web development,W3C,tutorials,programming,training,learning,quiz,primer,lessons,references,examples,
exercises,source code,colors,demos,tips,digital services,digital solutions,online solutions,support,
icrypt, icrypt technology, digital help,remote services,best tech company in africa,top 5 tech company
in africa,'''
META_DESCRIPTION= '''Icrypt Technology is a Technology Company which focus on Rendering of digital services,
 like building of websites,mobile apps, desktop apps,remote help,virtual assistance,graphics designs,
 custom services,'''


# Use by django_debug toolbar
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]