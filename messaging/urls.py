from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inbox, message_detail, send_message, archive_message,archived_messages  # ✅ Import views properly

urlpatterns = [
    # Messaging Views
    path('', inbox, name='inbox'),  
    path('<int:pk>/', message_detail, name='message_detail'),
    path('send/', send_message, name='send_message'),
    path('<int:pk>/archive/', archive_message, name='archive_message'),
    path('archived/', archived_messages, name='archived_messages'),

    # Password Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
]
