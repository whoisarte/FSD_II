from django.urls import path
from .views import HomePageView, AboutPageView, ContentPageView

urlpatterns = [
    path('about', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'index'),
    path('content', ContentPageView.as_view(), name = 'content')
]