from this import s
from .models import QuoteCard
from rest_framework import serializers

class QuoteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCard
        fields = ['id', 'quote', 'quoteAuthor']