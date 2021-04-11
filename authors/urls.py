from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [

    path('', views.allauthors, name="allauthors"),
    path('<str:key>/', views.detailauthor, name="detailauthor"),
    path('<str:name>/allquotes', views.allauthorquotes, name="allauthorquotes"),
]