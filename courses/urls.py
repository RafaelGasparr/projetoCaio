

from django.urls import path
from .views import CursosView

urlpatterns = [
    path('', CursosView.as_view(), name='course_list'),
]
