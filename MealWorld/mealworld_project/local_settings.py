# mealworld_project/local_settings.py

SECRET_KEY = 'django-insecure-*ojk5qrtg^@3w^t*uid5r#yfujw#h*tl%#1vp5l(%cbjs!0vle'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mealworld',
        'USER': 'mealworldadmin',
        'PASSWORD': '000000',
        'HOST': 'localhost',
        'PORT': '5432',  # Default PostgreSQL port
    }
}

# (Optional) Add other sensitive credentials here:
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# STRIPE_SECRET_KEY = ''
