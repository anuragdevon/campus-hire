"""
ASGI config for placementMangement project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

current_module = os.getenv("DJANGO_SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", current_module)

application = get_asgi_application()
