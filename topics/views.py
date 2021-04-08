from django.shortcuts import render, get_object_or_404
from search.models import Quotes


# Create your views here.
def alltopics(request):
    topics = ["life", "love", "war"]
    return render(request, "topics/alltopics.html", {"topics": topics})

def detail(request, topic):
    results = Quotes.objects.filter(topics__contains=topic)
    return render(request, "topics/detail.html", {"results": results})