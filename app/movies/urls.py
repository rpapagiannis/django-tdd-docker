from django.urls import path
from .views import MovieViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'api/movies', MovieViewSet, basename='movie')
urlpatterns = router.urls
