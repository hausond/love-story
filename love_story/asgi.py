"""
ASGI config for love_story project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "love_story.settings")

application = get_asgi_application()
