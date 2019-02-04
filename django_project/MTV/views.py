from django.shortcuts import render, redirect
from MTV.models import Topic, WebPage, AccessRecords


# Create your views here.

def index(request):
    webpages_list = AccessRecords.objects.order_by('date')
    topic_list = Topic.objects.order_by('top_name')
    data_dict = {'access_records': webpages_list, 'topic_list': topic_list}
    return render(request, 'MTV/index.html', context=data_dict)

