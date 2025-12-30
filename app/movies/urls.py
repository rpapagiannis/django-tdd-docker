from rest_framework import routers

from .views import MovieViewSet

router = routers.SimpleRouter()
router.register(r"api/movies", MovieViewSet, basename="movie")
urlpatterns = router.urls
