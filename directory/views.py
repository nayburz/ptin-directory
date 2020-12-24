
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, query
from django.db.models.functions import Concat
from django.db.models import CharField, Value
from django.shortcuts import get_object_or_404

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
        

    # puts together first name and last name into query as 'full_name'

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


        # State
        if 'region' in self.request.GET:
            state = self.request.GET['region']
            if state:
                query_list = query_list.filter(state__iexact=state)      
        
        return query_list


    # def get_state_queryset(self): # new
    #         return Person.objects.filter(
    #             Q(state__iexact='Montana')
    #         )

        
        


class StateView(ListView):
    model = Person
    template_name = "state_lists.html"

    def get_state_queryset(self):
        self.state = get_object_or_404(Person, state=self.kwargs['state'])
        return Person.objects.filter(state=self.state)

