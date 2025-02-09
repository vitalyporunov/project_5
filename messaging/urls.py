from django.urls import path
from . import views  

urlpatterns = [
    path('', views.inbox, name='inbox'),  # ✅ Inbox view
    path('send/', views.send_message, name='send_message'),  # ✅ Send message view
    path('<int:pk>/', views.message_detail, name='message_detail'),  # ✅ Message detail view
    path('archived/', views.archived_messages, name='archived_messages'),  # ✅ Archive message view
]
