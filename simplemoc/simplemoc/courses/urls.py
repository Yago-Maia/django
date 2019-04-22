from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.details, name='details'),
    path('<slug>/incricao/', views.enrollment, name='enrollment'),
    path('<slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('<slug>/anuncios/', views.announcements, name='announcements'),
]