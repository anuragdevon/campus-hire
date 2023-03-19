"""
WSGI config for placementMangement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

current_module = os.getenv("DJANGO_SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", current_module)

application = get_wsgi_application()
