from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/', views.all_projects, name='all_projects'),
]
