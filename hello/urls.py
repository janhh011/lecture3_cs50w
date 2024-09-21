#which urls do we have?
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jan", views.jan, name="jan"),
    path("<str:name>", views.greet_html, name="greet_html")
]