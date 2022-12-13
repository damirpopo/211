from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Stat

def index(request):
    stat = Stat.objects.all()
    return render(request, "index.html", {"stat": stat})

def create(request):
    if request.method == "POST":
        stat = Stat()
        stat.title = request.POST.get("title")
        stat.subtile = request.POST.get("subtile")
        stat.URL = request.POST.get("URL")
        stat.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        stat = Stat.objects.get(id=id)
        if request.method == "POST":
            stat.title = request.POST.get("title")
            stat.subtile = request.POST.get("subtile")
            stat.URL = request.POST.get("URL")
            stat.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html",{"stat": stat})
    except Stat.DoesNotExist:
        return HttpResponseNotFound("<h2>stat not found</h2>")


def delete(request, id):
    try:
        stat = Stat.objects.get(id=id)
        stat.delete()
        return HttpResponseRedirect("/")
    except Stat.DoesNotExist:
        return HttpResponseNotFound("<h2>stat not found</h2>")
