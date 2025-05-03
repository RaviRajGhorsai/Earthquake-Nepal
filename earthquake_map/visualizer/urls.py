from django.urls import path
from .views import map_view, home_view

urlpatterns = [
     path('', home_view, name='home'),
     path('map/', map_view, name='map'),
]
