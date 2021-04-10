from django.shortcuts import render
from .models import Authors

# Create your views here.
def allauthors(request):
    authors = Authors.objects.all().order_by('-name')
    authorstable = {}
    for author in authors:
        authorstable[author.name] = Authors.objects.filter(name=author.name).count()


    return render(request,"authors/allauthors.html",{"authorstable":authorstable})