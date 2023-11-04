from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProj, name="create-project"),
    path('update-project/<str:pk>', views.updateProj, name="update-project"),
    path('delete-project/<str:pk>', views.deleteProj, name="delete-project"),
]
