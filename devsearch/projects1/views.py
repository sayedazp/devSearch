from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def projects(reqeust):
    
    msg = "hi there"
    return render(reqeust, 'projects/projects.html', {'msg':msg, 'projects':Project.objects.all()})

def project(reqeust, pk):
    projy = Project.objects.get(id = pk)
    return render(reqeust, 'projects/single-project.html', {'project':projy})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)