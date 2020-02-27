from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=300)
    date = models.DateField(auto_now_add=True)
    # add in thumbnail later
    # add in author later
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50]+'...'