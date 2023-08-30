from django.urls import path

from . import views

app_name = "chassis"
urlpatterns = [
    path("", views.index, name="index"),
]
