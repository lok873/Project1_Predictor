from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def dynamic(request):
    country1 = request.GET['selectcountry1']
    country2 = request.GET['selectcountry2']
    # country2 = request.GET['c2']
    # print(country1)
    
    countries = {
        "coun1" : country1,
        "coun2" : country2,
    }
    # print(countries)
    # print(country1)
    return render(request, "dynamic.html", context=countries)