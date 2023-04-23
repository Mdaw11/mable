from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView, ManageUsersView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('manage-users/', ManageUsersView.as_view(), name='manage-users'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('admin_home/', views.admin_homepage, name='admin_home'),
    path('developer_home/', views.developer_homepage, name='developer_home'),
    path('project_manager_home/', views.project_manager_homepage, name='project_manager_home'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]