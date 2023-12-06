from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="index"),
    path("ver_guitarras/", views.view_guitarras, name="stock")
]
