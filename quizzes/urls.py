# quizzes/urls.py

from django.urls import path
from . import views  # Import views from the quizzes app

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),  # Example URL pattern
]
