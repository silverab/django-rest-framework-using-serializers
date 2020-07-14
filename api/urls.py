from django.urls import path
from api import views


urlpatterns = [
    path('', views.apiOverview, name='api-overeview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-list/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
]