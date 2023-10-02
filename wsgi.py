"""
WSGI config for library project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

application = get_wsgi_application()

# ALTER ROLE hamzoooz SET client_encoding TO 'utf8';
# ALTER ROLE hamzoooz SET default_transaction_isolation TO 'read committed';
# ALTER ROLE hamzoooz SET timezone TO 'UTC';