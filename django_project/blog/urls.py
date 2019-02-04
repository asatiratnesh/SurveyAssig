from django.urls import path
from blog import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.AboutView.as_view(), name='about'),
    url(r'^$', views.AboutView.as_view(), name='logout'),

]
