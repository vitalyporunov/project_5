from django.urls import path
from .views import project_list, project_detail, project_create, restricted_view

urlpatterns = [
    path('', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
]
