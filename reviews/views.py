from django.views.generic import ListView
from .models import Review

class HomePageView(ListView):
    template_name = 'home.html'
    model = Review
