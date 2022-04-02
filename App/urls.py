from django.urls import path

from . import views
from .views import Affiche_ListView, CreateProject, delete, deleteGeneric

urlpatterns=[
    path('index/', views.index),
    path ('index_c/<int:classe>/', views.index_id),
    path('template/', views.template),
    path('Affiche/',views.Affiche),
    path('Affiche_listview/', Affiche_ListView.as_view(),name="LV"),
    path('Ajout/',views.add_project,name="ajout"),
    path('CreateP/',CreateProject.as_view()),
    path('<id>/delete',delete, name="delete"),
    path('deleteP/<int:pk>',deleteGeneric.as_view(),name="DD"),
    path('Accueil/',views.Acceuil, name="acceuil"),
    path('Login/',views.Login, name="login"),
    path('register/',views.register, name="register")
]