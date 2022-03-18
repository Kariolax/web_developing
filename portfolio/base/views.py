from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Entry, Message, Link
from django.db.models import Q
from collections import OrderedDict

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else 'home'
    entries = Entry.objects.filter(
        Q(topic__name__icontains=q)
    )

    topics = Topic.objects.all()
    context = {'entries': entries, 'topics': topics}
    return render(request, 'base/home.html', context)


def external_url_github(request):
    return redirect(str(Link.objects.get(link__icontains='github')))


def external_url_linkedin(request):
    return redirect(str(Link.objects.get(link__icontains='linkedin')))
