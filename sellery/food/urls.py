from django.urls import path

from . import views

urlpatterns = [
    path('', views.FoodView.as_view(), name="food"),
]