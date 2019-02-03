from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostsListCreate.as_view()),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
]
