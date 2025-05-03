from django.urls import path
from . import views

urlpatterns = [
    path("heart/", views.heart_predict.as_view())
]
