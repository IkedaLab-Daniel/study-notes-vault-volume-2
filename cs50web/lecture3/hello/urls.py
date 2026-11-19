from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ice", views.ice, name="ice"),
    path("<str:name>", views.greet, name="greet"),
]