from django.shortcuts import render
from .models import Entry
from django.contrib.auth.decorators import login_required

def entry_list(request):
    entries = Entry.objects.all().order_by('date')
    return render(request, 'dailyjournal/entries.html', {'entries': entries})

def entry_detail(request,slug):
    entry = Entry.objects.get(slug=slug)
    return render(request, 'dailyjournal/entry.html', {'entry' : entry})

@login_required(login_url="/accounts/login/")
def entry_create(request):
    return render(request, 'dailyjournal/create.html')