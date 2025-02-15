from .models import Quote
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import QuoteSerializer
from django.conf import settings
import random

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class RandomQuoteView(views.APIView):
    def get(self, request):
        print("Headers:", request.headers.get('Authorization'))
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Missing Authorization header'}, status=401)

        auth_parts = auth_header.split()
        if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
            return Response({'error': 'Invalid Authorization header'}, status=401)

        api_key = auth_parts[1]
        if api_key != settings.API_KEY:
             return Response({'error': 'Invalid API key'}, status=401)

         # If the API key is valid, proceed with the serialization of the random quote
        quotes = Quote.objects.all()
        random_quote = random.choice(quotes)
        serializer = QuoteSerializer(random_quote)
        return Response(serializer.data)
