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

# ✅ Project Creation View
@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user  # Link the project to the logged-in user
            project.save()

            if hasattr(project, 'stakeholders'):  
                project.stakeholders.add(request.user)  # Add user as stakeholder if applicable

            return redirect('project_list')  # Redirect after successful creation
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form})

# ✅ Role-Based Access (For Managers Only)
def is_manager(user):
    return hasattr(user, 'role') and user.role == 'manager'  # Safe role checking

@user_passes_test(is_manager)
def restricted_view(request):
    return render(request, 'restricted.html')
