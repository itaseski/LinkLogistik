from django.urls import path

from . import views

app_name = "spares"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:document_id>/", views.detail, name="detail"),
]