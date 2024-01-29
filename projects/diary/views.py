from django.shortcuts import render

def index(request):
    return render(request, "diary/day_list.html")
# Create your views here.
