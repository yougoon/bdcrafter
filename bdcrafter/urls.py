from django.contrib import admin
from django.urls import path

from core.views import home, contact_submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact-submit/', contact_submit, name='contact_submit'),
]