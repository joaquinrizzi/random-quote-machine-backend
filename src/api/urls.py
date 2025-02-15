from . import views
from django.urls import path, include
from rest_framework import routers
from .views import QuoteViewSet, RandomQuoteView

router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)


urlpatterns = [
    path('random_quote/', RandomQuoteView.as_view(), name='random_quote'),
    path('', include(router.urls), name="all_quotes"),

]
