from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Project
from django.core.paginator import Paginator
from .forms import ProjectForm
from django.db.models import Q
from tickets.models import Ticket
from users.models import CustomUser

# Create your views here.
class ProjectHomeView(View):
    def get(self, request):
        projects = Project.objects.all()
        search_query = request.GET.get('search')
        if search_query:    
            projects = Project.objects.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        paginator = Paginator(projects, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'projects': projects, 
                   'page_obj': page_obj, 
                   'search_query': search_query}
        return render(request, 'projects/project_home.html', context)

class ProjectView(View):
    def get(self, request, pk):
        projects = Project.objects.get(id=pk)
        search_query = request.GET.get('search')
        tickets = Ticket.objects.filter(project=projects)
        # Get assignees of all tickets for this project
        assignees = CustomUser.objects.filter(assignee__in=tickets).distinct()
        
        # Search functionality
        if search_query:
            tickets = tickets.filter(
                Q(assignee__username__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(status__iexact=search_query) |
                Q(priority__icontains=search_query) |
                Q(type__icontains=search_query)
            )
            assignees = assignees.filter(username__icontains=search_query)

        ticket_assignees = {}
        
        for ticket in tickets:
            ticket_assignees[ticket] = ticket.assignee.all()
            
        # Paginate the ticket table
        paginator = Paginator(tickets, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Paginate the assignees table
        assignees_paginator = Paginator(assignees, 5)
        assignees_page_number = request.GET.get('assignees_page')
        assignees_page_obj = assignees_paginator.get_page(assignees_page_number)
        
            

        context = {
            'projects': projects, 
            'tickets': tickets,
            'page_obj': page_obj,
            'assignees': assignees_page_obj,
            'search_query': search_query
        }

        return render(request, 'projects/project.html', context)

    def post(self, request, pk):
        # Handle POST requests
        return redirect('project', pk=pk)

@method_decorator(login_required, name='dispatch')
class CreateProjectView(View):
    def get(self, request):
        form = ProjectForm()
        context = {'form': form}
        return render(request, 'projects/project_home.html', context)

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-home')
        else:
            context = {'form': form}
            return render(request, 'projects/project_home.html', context)

@method_decorator(login_required, name='dispatch')
class UpdateProjectView(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        context = {'form': form, 'project': project}
        return render(request, 'projects/project_home.html', context)

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project', pk=project.id)
        else:
            context = {'form': form, 'project': project}
            return render(request, 'projects/project_home.html', context)

@method_decorator(login_required, name='dispatch')
class DeleteProjectView(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        return render(request, 'projects/project-delete.html', {'obj': project})

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('project-home')