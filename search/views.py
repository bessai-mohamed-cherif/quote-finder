from django.shortcuts import render
from .models import Quotes

# Create your views here.

def homepage(request):
    return render(request,"search/homepage.html")

def searchresult(request):
    query = request.GET.get('q')
    results = Quotes.objects.filter(phrase__contains=query)
    return render(request, "search/searchresult.html", {'results': results, 'error':"there is no quotes."})
