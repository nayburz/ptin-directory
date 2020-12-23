from django.urls import path

from .views import HomePageView, DirectoryListView, DirectoryDetailView, SearchResultsView

app_name = 'directory'

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('ptin-directory/', DirectoryListView.as_view(), name='directory-list'),
    path('ptin-directory/<int:pk>', DirectoryDetailView.as_view(), name='person-detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]