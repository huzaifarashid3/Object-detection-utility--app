from django.urls import path
from . import views
app_name = 'finezy'
urlpatterns = [
    path("", views.index, name="index"),
    path("detect", views.detect, name="detect"),
    path("results", views.results, name="results"),
]