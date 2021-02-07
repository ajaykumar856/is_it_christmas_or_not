from django.shortcuts import render
import datetime
now =  datetime.datetime.now()

# Create your views here.

def dark(request):
    return render(request,"christmas/dark.html",{
        "christmas" : now.month==12 and now.day==25
    })
