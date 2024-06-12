# quizzes/views.py

from django.shortcuts import render

def quiz_list(request):
    return render(request, 'quizzes/quiz_list.html')  # Render a template
