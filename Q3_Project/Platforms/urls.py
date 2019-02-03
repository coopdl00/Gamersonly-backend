from django.urls import path

from . import views

urlpatterns = [
    path('api/platforms/', views.PlatformsListCreate.as_view()),
]
