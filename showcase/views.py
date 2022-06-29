
from django.views.generic import TemplateView, ListView
from .models import Menu


class HomePageView(ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"
