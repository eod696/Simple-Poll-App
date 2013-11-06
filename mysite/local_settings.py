# Admin user info:
# U: dan
# P: Senhiser7

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                 # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'C:/Users/Dan/Workspaces/DjangoTut1/data.db',   # Or path to database file if using sqlite3.
        
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',     # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',     # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []

MEDIA_ROOT = 'C:/Users/Dan/Workspaces/DjangoTut1/mysite/media'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'C:/Users/Dan/Workspaces/DjangoTut1/static',
)

TEMPLATE_DIRS = (
    'C:/Users/Dan/Workspaces/DjangoTut1/templates',
)