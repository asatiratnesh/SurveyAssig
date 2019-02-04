from django.urls import path
from mymodel import views


urlpatterns = [
    path('cities', views.CitiesListView, name='cityhome'),
    path('', views.MyCityList, name='home'),
    path('cities/add', views.addCity, name='addcity'),

]
