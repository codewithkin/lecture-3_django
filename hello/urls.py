from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("brian", views.brian,name=""),
    path("david", views.david,name="david"),
    path("kin", views.kin, name="kin"),
    path("<str:name>", views.greet, name="greet")
]