"""
WSGI config for love_story project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "love_story.settings")

application = get_wsgi_application()
