from django.urls import path
from . import views

urlpatterns = [
    path('pessoas', views.index, name='index'),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("remove", views.removeFinal, name="remove"),
]