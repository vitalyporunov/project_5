from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),                        
    path('<int:pk>/', views.project_detail, name='project_detail'),       
    path('create/', views.project_create, name='create_project'), 
    path('<int:pk>/update/', views.project_update, name='update_project'),  
    path('<int:pk>/delete/', views.project_delete, name='delete_project'),  
]
