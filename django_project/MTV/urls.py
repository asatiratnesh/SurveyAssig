from django.urls import path
from MTV import views


urlpatterns = [
    path('', views.index, name='index'),

]
