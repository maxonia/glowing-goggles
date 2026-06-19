from django.urls import path, include
from . import views
from .views import register_view
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login_view, name='login'),
    path('register/', register_view, name='register'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('profile/', views.profile_view, name='profile'),
    path('add-event/', views.add_event, name='add_event'),
    path('notes/', include('notes.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('policy/', TemplateView.as_view(template_name='policy.html'), name='policy'),
]
