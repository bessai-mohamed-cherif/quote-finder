from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"search/homepage.html")

def searchresult(request):
    return render(request, "search/searchresult.html")
