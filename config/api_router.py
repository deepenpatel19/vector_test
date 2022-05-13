from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from vector_test.users.api.views import UserViewSet
from vector_test.wikipedia.urls import register_wikipedia_urls

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
register_wikipedia_urls(router)


app_name = "api"
urlpatterns = router.urls
