from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet, FictionViewSet, NonFictionViewSet, ScienceViewSet,
    HistoryViewSet, MysteryViewSet, FantasyViewSet, BiographyViewSet,
    RomanceViewSet, ThrillerViewSet, PoetryViewSet
)

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('fiction', FictionViewSet, basename='fiction')
router.register('nonfiction', NonFictionViewSet, basename='nonfiction')
router.register('science', ScienceViewSet, basename='science')
router.register('history', HistoryViewSet, basename='history')
router.register('mystery', MysteryViewSet, basename='mystery')
router.register('fantasy', FantasyViewSet, basename='fantasy')
router.register('biography', BiographyViewSet, basename='biography')
router.register('romance', RomanceViewSet, basename='romance')
router.register('thriller', ThrillerViewSet, basename='thriller')
router.register('poetry', PoetryViewSet, basename='poetry')

urlpatterns = router.urls
