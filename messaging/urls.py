from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send_message'),
    path('<int:pk>/', views.message_detail, name='message_detail'),
    path('<int:pk>/archive/', views.archive_message, name='archive_message'),
    ]