from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page = 'polls:home'), name='logout'),
    path('cadastro/', views.register, name='register'),
    path('editar/', views.edit, name='edit'),
] 