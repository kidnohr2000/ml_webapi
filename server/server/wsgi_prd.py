"""
WSGI config for apps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

pth = os.path.join(os.path.dirname(__file__), '..')
if pth not in sys.path:
    sys.path.insert(1, pth)
del pth

application = get_wsgi_application()
