from django.test import TestCase
from .models import Quote
# Create your tests here.


class QuoteTestCase(TestCase):
    def setUp(self):
        self.test_quote = Quote.objects.create(content="Test Quote", author="Test Author")

    def test_quote_was_created(self):
        self.assertTrue(self.test_quote.pk)

    def test_quote_content(self):
        self.assertEqual(self.test_quote.content, "Test Quote")

    def test_quote_author(self):
        self.assertEqual(self.test_quote.author, "Test Author")
