from django.http import HttpResponse
from rest_framework import viewsets
from .models import BookData
from .serializers import BookSerializer

def index(request):
    # Root URL view
    return HttpResponse(
        "<h1>Welcome to the Book API!</h1>"
        "<p>Go to <a href='/api/books/'>/api/books/</a> to view the API.</p>"
    )

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

# 10 Category-Specific ViewSets
class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fiction')
    serializer_class = BookSerializer

class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Non-Fiction')
    serializer_class = BookSerializer

class ScienceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Science')
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='History')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Biography')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Thriller')
    serializer_class = BookSerializer

class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Poetry')
    serializer_class = BookSerializer
