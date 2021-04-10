from django.shortcuts import render
from .models import Authors

# Create your views here.
def allauthors(request):
    authors = Authors.objects.all().order_by('-name')
    authorstable = {}
    for author in authors:
        authorstable[author.name] = Authors.objects.filter(name=author.name).count()
    return render(request,"authors/allauthors.html",{"authorstable":authorstable})

def detailauthor(request, key):
    authors = Authors.objects.filter(name=key)
    print(authors)
    return render(request, "authors/detailauthor.html", {'authors': authors})