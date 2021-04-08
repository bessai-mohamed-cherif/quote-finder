from django.shortcuts import render, get_object_or_404


# Create your views here.
def alltopics(request):
    topics = ["life", "love", "war"]
    return render(request,"topics/alltopics.html",{"topics":topics})

def detail(request, topic):
    return render(request, "topics/detail.html", {"topic": topic})