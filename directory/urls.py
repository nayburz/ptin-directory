from django.urls import path

from .views import HomePageView, DirectoryListView, DirectoryDetailView

app_name = 'directory'

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('ptin-directory/', DirectoryListView.as_view(), name='directory-list'),
    path('ptin-directory/<int:pk>', DirectoryDetailView.as_view(), name='directory-detail'),
]