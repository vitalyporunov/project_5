from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project
from .forms import ProjectForm

# ✅ Project List (Shows only user's projects)
@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)  # Show projects belonging to the logged-in user
    return render(request, 'projects/project_list.html', {'projects': projects})

# ✅ Project Detail View
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)  # Ensure users see only their projects
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Don't save to DB yet
            project.owner = request.user      # ✅ Assign the logged-in user as the owner
            project.save()                    # Now save to the DB
            form.save_m2m()                   # Save many-to-many relationships (if any)
            return redirect('projects')       # Redirect after creation
    else:
        form = ProjectForm()
    
    return render(request, 'projects/create_project.html', {'form': form})

# ✅ Role-Based Access (For Managers Only)
def is_manager(user):
    return hasattr(user, 'role') and user.role == 'manager'  # Safe role checking

@user_passes_test(is_manager)
def restricted_view(request):
    return render(request, 'projects/restricted.html')

