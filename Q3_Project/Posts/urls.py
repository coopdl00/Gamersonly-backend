from django.urls import path

from . import views

urlpatterns = [
    path('api/posts/', views.PostsListCreate.as_view()),
]
