from pathlib import Path

DEBUG                         = True
SECRET_KEY                    = 'django-insecure-p9(@x2p^o0p(&6ofm)4)ivgru!hxk5ni(-6-2#dp9!l$77lh(m'
ALLOWED_HOSTS                 = ['scds-ai.syndevops.com']
BASE_DIR                      = Path(__file__).resolve().parent.parent
ROOT_URLCONF                  = '_project_.urls'
WSGI_APPLICATION              = '_project_.wsgi.application'
LANGUAGE_CODE                 = 'en-us'
USE_TZ                        = True
TIME_ZONE                     = 'UTC'
USE_I18N                      = True
STATIC_URL                    = 'static/'
DEFAULT_AUTO_FIELD            = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK          = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home" 
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '_templates_'],
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

STATICFILES_DIRS = [
    BASE_DIR / "_static_",
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage", # CompressedManifestStaticFilesStorage
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
