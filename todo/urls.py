from django.urls import path
from . import views

# Unique identifier for the urls
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]