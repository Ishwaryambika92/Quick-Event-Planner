from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('delete/<int:pk>/', views.delete_event, name='delete_event'),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='quickapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    
    

    path('register/<int:id>/', views.register_event, name='register_event')
]
