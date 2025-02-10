from django.urls import path
from . import views  

urlpatterns = [
    path('', views.project_list, name='projects'),           
    path('<int:pk>/', views.project_detail, name='project_detail'),  
    path('create/', views.project_create, name='create_project'),   
    path('restricted/', views.restricted_view, name='restricted_view'),  
]
