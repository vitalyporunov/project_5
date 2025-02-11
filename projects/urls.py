from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects'),                        # ✅ List all projects
    path('<int:pk>/', views.project_detail, name='project_detail'),       # ✅ View project details
    path('create/', views.project_create, name='create_project'),         # ✅ Create new project
    path('restricted/', views.restricted_view, name='restricted_view'),   # ✅ Restricted access view
]
