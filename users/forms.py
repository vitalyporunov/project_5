from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Register Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Added 'required' for clarity

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

# Login Form (Simplified)
class LoginForm(AuthenticationForm):
    pass  # ✅ Using default fields unless customization is needed

# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role']  # Ensure 'role' exists in CustomUser
