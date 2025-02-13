from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  

urlpatterns = [
    path('', views.inbox, name='inbox'),  
    path('send/', views.send_message, name='send_message'),  
    path('<int:pk>/', views.message_detail, name='message_detail'),  
    path('<int:pk>/archive/', views.archive_message, name='archive_message'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
]
