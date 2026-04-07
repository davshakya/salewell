import sys
import os

# Add your project path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Load Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()