# plataforma_ensino/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

@login_required
def home(request):
    return render(request, 'home.html')



def test_static_view(request):
    return render(request, 'test_static.html')

def home(request):
    return render(request, 'home.html')

class CursosView(TemplateView):
    template_name = 'cursos.html'