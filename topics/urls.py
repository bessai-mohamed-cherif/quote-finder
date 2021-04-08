from django.urls import path
from . import views

app_name = "topics"

urlpatterns = [

    path('', views.alltopics, name="alltopics"),
    path('<str:topic>/', views.detail, name="detail"),
]