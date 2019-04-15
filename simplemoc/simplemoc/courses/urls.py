from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.details, name='details'),
]