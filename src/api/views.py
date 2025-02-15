from .models import Quote
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import QuoteSerializer
import random

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class RandomQuoteView(views.APIView):
    def get(self, request):
        quotes = Quote.objects.all()
        random_quote = random.choice(quotes)
        serializer = QuoteSerializer(random_quote)
        return Response(serializer.data)
