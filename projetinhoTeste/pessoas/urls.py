from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add, name="add"),
    # pedindo parametro do tipo int ->  <1>tipo : nome do parametro
    path("edit/<int:pessoa_id>/", views.edit, name="edit"),
    path("remove/<int:pessoa_id>/", views.remove, name="remove"),
    path("remove/final/<int:pessoa_id>/",
         views.removeFinal, name="removeFinal"),
    path("", views.index, name="index"),  # list - read -> Caminho vazio
]
