
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, query
from django.db.models.functions import Concat
from django.db.models import CharField, Value

from .models import Person


class HomePageView(TemplateView):
    template_name = 'home.html'

class DirectoryListView(ListView):
    model = Person
    template_name = 'person_list.html'

class DirectoryDetailView(DetailView):
    model = Person
    template_name = "person_detail.html"

class SearchResultsView(ListView):
    model = Person
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        query_list = Person.objects.all()
        

    # puts together first name and last name

        if query:
            query_list = query_list.annotate(
                full_name=Concat(
                    'first_name',
                    Value(' '),
                    'last_name',
                    output_field=CharField()
                )
            ).filter(
                Q(full_name__icontains=query)

        )
        return query_list