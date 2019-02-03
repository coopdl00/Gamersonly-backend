from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UsersListCreate.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),
]
