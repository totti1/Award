from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddProjectForm, AddProfileForm
from .models import Profile, Project

# Create your views here.
def home(request):
    current_user = request.user
    projects = Project.get_all_projects()
    return render(request, 'home.html', {"projects": projects, "user": current_user})


@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    profile = Profile.get_profile(current_user)
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
        return redirect('home')

    else:
        form = AddProjectForm()
    return render(request, 'add_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = AddProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.get_profile(current_user)
    if profile == None:
        return redirect('upload_profile')
    else:
        project = Project.get_projects_by_id(profile.id)
        return render(request, 'profile.html', {"project": project, "profile": profile})
