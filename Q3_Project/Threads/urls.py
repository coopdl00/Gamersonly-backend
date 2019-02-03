from django.urls import path

from . import views

urlpatterns = [
    path('api/threads/', views.ThreadsListCreate.as_view()),
]
