from django.shortcuts import render

# Create your views here.
def allauthors(request):
    return render(request,"authors/allauthors.html")