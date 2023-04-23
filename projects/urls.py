from django.urls import path
from .views import ProjectHomeView, ProjectView, CreateProjectView, UpdateProjectView, DeleteProjectView


urlpatterns = [
    path('projects/', ProjectHomeView.as_view(), name='project-home'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    path('project/create', CreateProjectView.as_view(), name='create-project'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update-project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete-project'),
]