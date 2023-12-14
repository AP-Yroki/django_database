from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<int:id>/', views.edit),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
    path('many_to_many/', views.index_many),
    path('create_many/', views.create_many),
]

