from django.urls import path

from .views import HomePageView, DirectoryListView, DirectoryDetailPage

app_name = 'directory'

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('ptin-directory/', DirectoryListView.as_view(), name='directory-list'),
]