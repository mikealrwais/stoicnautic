from django.shortcuts import render
from .models import Entry

def entry_list(request):
    entries = Entry.objects.all().order_by('date')
    context = {
        'entries': entries,
    }
    return render(request, 'dailyjournal/entries.html', context)
