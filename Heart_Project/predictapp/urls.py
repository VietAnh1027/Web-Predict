from django.urls import path
from . import views

urlpatterns = [
    path("", views.heart_predict.as_view()),
]
