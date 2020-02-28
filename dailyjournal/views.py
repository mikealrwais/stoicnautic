from django.shortcuts import render, HttpResponse
from .models import Entry

def entry_list(request):
    entries = Entry.objects.all().order_by('date')
    context = {
        'entries': entries,
    }
    return render(request, 'dailyjournal/entries.html', context)

def entry_detail(request,slug):
    return HttpResponse(slug)
