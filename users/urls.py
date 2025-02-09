from django.urls import path
from .views import register_view, login_view, logout_view, profile_update, profile_view  # ✅ Correct Import

urlpatterns = [
    path("register/", register_view, name="register"),        
    path("login/", login_view, name="login"),                 
    path("logout/", logout_view, name="logout"),              
    path('profile/', profile_view, name='profile'),           
    path('profile/update/', profile_update, name='profile_update'),  
]
