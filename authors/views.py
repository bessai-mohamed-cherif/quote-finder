from django.shortcuts import render
from .models import Authors

# Create your views here.
def allauthors(request):
    authors = Authors.objects.all().order_by('-name')
    return render(request,"authors/allauthors.html",{"authors":authors})