from django.urls import path
from dlist import views


urlpatterns = [
    path('', views.list, name='list'),
]