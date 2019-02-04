from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cities
from .forms import AddCityForm

# Create your views here.


def CitiesListView(request):
    list_of_cities = Cities.objects.order_by('-name')
    template = loader.get_template('mymodel/cities.html')
    context = {
        'list_of_cities': list_of_cities
    }
    return HttpResponse(template.render(context, request))


def MyCityList(request):
    list_of_cities = Cities.objects.order_by('name')
    context = {'list_of_cities': list_of_cities,}
    return render(request, 'mymodel/cities.html', context)


def addCity(request):
    if request.method == 'POST':
        form = AddCityForm(request.POST)

        if form.is_valid():
            new_city = Cities(name=request.POST['name'])
            new_city.save()
            return redirect('cityhome')
    else:
        form = AddCityForm()

    context = {'form': form}
    return render(request, 'mymodel/add_cities.html', context)

