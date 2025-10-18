from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-%%$%87i_2cknxdhk*b3t1164c@6i0r)v(e*85^4!ij7d7s)8wu')

DEBUG = False

ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', "localhost", '.now.sh', '.onrender.com']
AUTH_USER_MODEL='users.CustomUser'
CSRF_TRUSTED_ORIGINS=["https://*.onrender.com","http://127.0.0.1:8000", "https://*.vercel.app"]

# Application definition
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'events',
    'users',
    'core',
    
]


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

# Debug Toolbar Configuration for Production
INTERNAL_IPS = [
    "127.0.0.1",
]

# Allow debug toolbar to work on Vercel
def show_toolbar(request):
    return True

""" DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
} """

ROOT_URLCONF = 'event_management.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'event_management.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres.pexcruhmgmmprreluruc',
        'PASSWORD': '4#B8_iVw!Jn+C3K',
        'HOST': 'aws-1-ap-south-1.pooler.supabase.com',
        'PORT': 6543,
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# For development - load static files from static folder
if not os.environ.get('VERCEL_ENV'):
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Use basic static files storage for Vercel
if os.environ.get('VERCEL_ENV'):
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
else:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_FROM = 'zishanahmed344@gmail.com'
EMAIL_HOST_USER = 'zishanahmed344@gmail.com'
EMAIL_HOST_PASSWORD = 'lcmh qfid cymj nite'
PASSWORD_RESET_TIMEOUT = 14400


FRONTEND_URL ="django-event-management-2.onrender.com"
# FRONTEND_URL ="https://django-event-management-wheat.vercel.app"
# FRONTEND_URL ="http://127.0.0.1:8000"
