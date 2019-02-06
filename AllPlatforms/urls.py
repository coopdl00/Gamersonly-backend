from django.urls import path

from . import views

urlpatterns = [
    path('allplatforms/', views.AllPlatformsListCreate.as_view()),
    path('allplatforms/<int:pk>/', views.AllPlatformsDetail.as_view()),
]
