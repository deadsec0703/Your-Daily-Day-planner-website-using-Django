from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
import requests
import json
import urllib.request
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("user_login")

def weath(request):
  try: 
    if request.GET.get("city"):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c6e315d09197cec231495138183954bd'
        city = request.GET.get("city")
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
        
        }
        context = {'weather' : weather}
        return render(request, 'weath.html',context) #returns the index.html template
  except:
        data ={}
        return render(request, "weath1.html", {"msg":"city name not found"})
  return render(request, "weath1.html")
def addtask(request):
    if request.method == "POST":
        f = TodoForm(request.POST)
        if f.is_valid():
            f.save()
            fm = TodoForm()
            return render(request, "addtask.html",{"fm":fm,"msg":'task saved'})
        
        else:
            return render(request, "addtask.html",{"fm":f,"msg":'check errors'})

    else:
        fm = TodoForm()
        return render(request, "addtask.html",{"fm":fm})
@login_required
def showtask(request):
    data = TodoModel.objects.filter(user=request.user)
    context = {"data":data}
    return render(request, "showtask.html",context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tasks = TodoModel.objects.filter(task__contains = searched)

        context = {
            'searched': searched,
            'tasks': tasks,
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', { })


def deletetask(request, id):
    dt = TodoModel.objects.get(pk = id)
    dt.delete()
    return redirect("showtask")

def weath1(request):
    return render(request, "weath1.html")