import sys
import os

sys.path.insert(0, '/home/bdcrafte/public_html')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bdcrafter.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()