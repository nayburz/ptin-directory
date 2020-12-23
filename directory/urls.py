from django.urls import path

from .views import HomePageView, DirectoryListView

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('ptin-directory/', DirectoryListView.as_view(), name='directory-list'),
]