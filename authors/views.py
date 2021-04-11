from django.shortcuts import render
from .models import Authors
from search.models import Quotes

# Create your views here.
def allauthors(request):
    authors = Authors.objects.all().order_by('-name')
    authorstable = {}
    for author in authors:
        authorstable[author.name] = Quotes.objects.filter(author=author.name).count()
    return render(request,"authors/allauthors.html",{"authorstable":authorstable})

def detailauthor(request, key):
    authors = Authors.objects.filter(name=key)
    return render(request, "authors/detailauthor.html", {'authors': authors})

def allauthorquotes(request, name):
    quotes = Quotes.objects.filter(author=name)
    return render(request, "authors/allauthorquotes.html", {'quotes': quotes})