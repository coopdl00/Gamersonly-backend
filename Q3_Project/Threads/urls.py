from django.urls import path

from . import views

urlpatterns = [
    path('threads/', views.ThreadsListCreate.as_view()),
    path('threads/<int:pk>/', views.ThreadsDetail.as_view()),
]
