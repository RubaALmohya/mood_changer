import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = ['web-mood-changer.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_app',
    'mood_app',
    'profile_app',
    'corsheaders',

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'mood_changer.urls'

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

WSGI_APPLICATION = 'mood_changer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Mood_Changer',
        'USER': 'postgres',
        'PASSWORD': '71112',
        'HOST': 'localhost',
    }
}
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=800)
DATABASES['default'].update(db_from_env)


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60*24),
'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
'ROTATE_REFRESH_TOKENS': False,
'BLACKLIST_AFTER_ROTATION': False,
'UPDATE_LAST_LOGIN': False,
'ALGORITHM': 'HS256',
'SIGNING_KEY': SECRET_KEY,
'VERIFYING_KEY': None,
'AUDIENCE': None,
'ISSUER': None,
'JWK_URL': None,
'LEEWAY': 0,
'AUTH_HEADER_TYPES': ('Bearer',),
'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
'USER_ID_FIELD': 'id',
'USER_ID_CLAIM': 'user_id',
'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
'TOKEN_TYPE_CLAIM': 'token_type',
'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
'JTI_CLAIM': 'jti',
'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
'SLIDING_TOKEN_LIFETIME': timedelta(minutes=60*24),
'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
