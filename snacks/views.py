from django.views.generic import TemplateView, ListView, DetailView
from .models import Snacks

class HomePageView(TemplateView):
    template_name='home.html'

class SnackListView(ListView):
    template_name ='snack_list.html'
    model = Snacks

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks

# Create your views here.
