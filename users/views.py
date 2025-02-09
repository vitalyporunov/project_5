from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileUpdateForm

# Registration View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm(request=request)  # ✅ Added request for context
    return render(request, "users/login.html", {"form": form})

# Logout View
@login_required  # ✅ Optional security measure
def logout_view(request):
    logout(request)
    return redirect("login")  # Ensure 'login' URL exists

# Profile Update View
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # ✅ Ensure this URL exists
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/profile_update.html', {'form': form})

# ✅ Optional Profile View
@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
