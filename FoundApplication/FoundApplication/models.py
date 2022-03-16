from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models

class QuoteCard(models.Model):
    quote = models.CharField(max_length=200)
    quoteAuthor = models.CharField(max_length=100)

    def __str__(self):
        return self.quoteAuthor
    
        
