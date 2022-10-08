from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),       # name is used for redirecting ex: <a href="{% url 'project' %}">

    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),   
]

