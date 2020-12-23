
from django.views.generic import TemplateView, ListView

from .models import Person


class HomePageView(TemplateView):
    template_name = 'home.html'

class DirectoryListView(ListView):
    model = Person
    template_name = 'person_list.html'