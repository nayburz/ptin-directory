from django.urls import path

from .views import (
    HomePageView, 
    DirectoryListView, 
    DirectoryDetailView, 
    SearchResultsView, 
    StateView,
    

)

app_name = 'directory'

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('ptin-directory/', DirectoryListView.as_view(), name='directory-list'),
    path('ptin-directory/<state>/', StateView.as_view()),   
    path('ptin-directory/<slug:slug>/', DirectoryDetailView.as_view(), name='person-detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]