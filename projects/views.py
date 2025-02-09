from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project
from .forms import ProjectForm

# ✅ Project List (Only for Authenticated Users)
@login_required
def project_list(request):
    projects = Project.objects.filter(stakeholders=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

# ✅ Project Detail View
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

# ✅ Project Creation View
@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            if hasattr(project, 'stakeholders'):  # ✅ Check if stakeholders exist
                project.stakeholders.add(request.user)
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# ✅ Role-Based Access (For Managers Only)
def is_manager(user):
    return hasattr(user, 'role') and user.role == 'manager'  # ✅ Safe role check

@user_passes_test(is_manager)
def restricted_view(request):
    return render(request, 'restricted.html')