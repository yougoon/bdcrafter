import sys
import os

# Add the project to Python path
sys.path.insert(0, '/home/bdcrafte/bdcrafter')

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'bdcrafter.settings'

# Import Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()