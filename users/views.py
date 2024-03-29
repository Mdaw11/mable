from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, developer_required, project_manager_required
from .models import CustomUser
from tickets.models import Ticket
from projects.models import Project

# Create your views here.
class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            if user.account_type == 'admin':
                return redirect(reverse('login'))
            elif user.account_type == 'developer':
                return redirect(reverse('login'))
            elif user.account_type == 'project_manager':
                return redirect(reverse('login'))
            # redirect to a success page
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        # Log out the user and redirect to the login page
        logout(request)
        return redirect('home')

class ManageUsersView(View):
    template_name = 'users/manage_users.html'
    paginate_by = 5
    
    def get(self, request, *args, **kwargs):
        # Get all users and tickets
        users = CustomUser.objects.all()
        projects = Project.objects.all()
        tickets = Ticket.objects.all()

        search_query = request.GET.get('search')
        if search_query:
            # Filter users based on the search query
            users = users.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(account_type__icontains=search_query)
            )

        # Paginate the ticket table
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'users': users, 'tickets': tickets, 'projects': projects, 'page_obj': page_obj, 'search_query': search_query}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Assign a ticket to an assignee
        if 'ticket' in request.POST:
            ticket_id = request.POST['ticket']
            assignee_id = request.POST['assignee']

            ticket = Ticket.objects.get(id=ticket_id)
            assignee = CustomUser.objects.get(id=assignee_id)

            ticket.assignee.set([assignee])
            ticket.save()
        
        # Assign a user to a project
        elif 'project' in request.POST:
            project_id = request.POST['project']
            assigned_users_id = request.POST['assigned_users']
            
            project = Project.objects.get(id=project_id)
            assigned_users = CustomUser.objects.get(id=assigned_users_id)
            
            project.assigned_users.set([assigned_users])
            project.save()

        return redirect('manage-users')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        user_created_tickets = Ticket.objects.filter(
            host=request.user
        ).order_by('-updated', '-created')

        user_assigned_tickets = Ticket.objects.filter(
            assignee=request.user
        ).order_by('-updated', '-created')

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'user_created_tickets': user_created_tickets,
            'user_assigned_tickets': user_assigned_tickets
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(self.success_url)

        user_created_tickets = Ticket.objects.filter(
            host=request.user
        ).order_by('-updated', '-created')

        user_assigned_tickets = Ticket.objects.filter(
            assignee=request.user
        ).order_by('-updated', '-created')

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'user_created_tickets': user_created_tickets,
            'user_assigned_tickets': user_assigned_tickets
        }

        return render(request, self.template_name, context)

    
@login_required
@admin_required
def admin_homepage(request):
    return render(request, 'users/admin_home.html')

@login_required
@developer_required
def developer_homepage(request):
    return render(request, 'users/developer_home.html')

@login_required
@project_manager_required
def project_manager_homepage(request):
    return render(request, 'users/project_manager_home.html')