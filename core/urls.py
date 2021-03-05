from django.urls import path
from .views import HomePageView,Sample

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', Sample.as_view(), name="sample"),
]