from posixpath import basename
from .viewsets import CountryViewSet, ContinentViewSet, CityViewSet


def register_wikipedia_urls(router):
    router.register("country", CountryViewSet, basename="country")
    router.register("continent", ContinentViewSet, basename="continent")
    router.register("city", CityViewSet, basename="city")
