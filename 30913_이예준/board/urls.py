from django.urls import path

from board import views


urlpatterns = [
    path('', views.main, name="main")
]