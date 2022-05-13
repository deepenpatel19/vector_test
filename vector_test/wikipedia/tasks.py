from requests import patch
from config import celery_app
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum
from .models import Continent, Country, City
from .decorators import city_area_and_population_validator, country_area_and_population_validator
import time

# Start: For Continent


@celery_app.task()
def list_continent(request, page_size=10):
    query = Continent.objects.filter().values().order_by("-id")

    paginator = PageNumberPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(query, request)
    return paginator.get_paginated_response(result_page)


@celery_app.task()
def create_continent(request):
    if request.data.get("name", ""):
        request.data["name"] = request.data["name"].capitalize()
    serializer = ContinentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Created"}, status=201)


def retrieve_continent(request, *args, **kwargs):
    instance = Continent.objects.filter(id=kwargs.get("pk")).values()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    return JsonResponse({"message": instance[0]}, status=200)


@celery_app.task()
def update_continent(request, *args, **kwargs):
    instance = Continent.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = ContinentSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=200)


@celery_app.task()
def partial_update_continent(request, *args, **kwargs):
    instance = Continent.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = ContinentSerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=206)


@celery_app.task()
def delete_continent(request, *args, **kwargs):
    instance = Continent.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    Continent.objects.filter(id=instance.id).delete()
    return JsonResponse({"message": "Deleted"}, status=204)

# End.

# Start: For Country


@celery_app.task()
def list_country(request, page_size=10):
    query = Country.objects.filter().values().order_by("-id")

    paginator = PageNumberPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(query, request)
    return paginator.get_paginated_response(result_page)


@country_area_and_population_validator
@celery_app.task()
def create_country(request):
    if request.data.get("name", ""):
        request.data["name"] = request.data["name"].capitalize()
    serializer = CountrySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Created"}, status=201)


def retrieve_country(request, *args, **kwargs):
    instance = Country.objects.filter(id=kwargs.get("pk")).values()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    return JsonResponse({"message": instance[0]}, status=200)


@country_area_and_population_validator
@celery_app.task()
def update_country(request, *args, **kwargs):
    instance = Country.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = CountrySerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=200)


@country_area_and_population_validator
@celery_app.task()
def partial_update_country(request, *args, **kwargs):
    instance = Country.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = CountrySerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=206)


@celery_app.task()
def delete_country(request, *args, **kwargs):
    instance = Country.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    Country.objects.filter(id=instance.id).delete()
    return JsonResponse({"message": "Deleted"}, status=204)

# End


# Start: For City


@celery_app.task()
def list_city(request, page_size=10):
    query = City.objects.filter().values().order_by("-id")

    paginator = PageNumberPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(query, request)
    return paginator.get_paginated_response(result_page)


@city_area_and_population_validator
@celery_app.task()
def create_city(request):
    if request.data.get("name", ""):
        request.data["name"] = request.data["name"].capitalize()
    serializer = CitySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Created"}, status=201)


def retrieve_city(request, *args, **kwargs):
    instance = City.objects.filter(id=kwargs.get("pk")).values()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    return JsonResponse({"message": instance[0]}, status=200)


@city_area_and_population_validator
@celery_app.task()
def update_city(request, *args, **kwargs):
    instance = City.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = CitySerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=200)


@city_area_and_population_validator
@celery_app.task()
def partial_update_city(request, *args, **kwargs):
    instance = City.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)

    serializer = CitySerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse({"message": "Updated"}, status=206)


@celery_app.task()
def delete_city(request, *args, **kwargs):
    instance = City.objects.filter(id=kwargs.get("pk")).first()
    if not instance:
        return JsonResponse({"message": "Not found."}, status=404)
    City.objects.filter(id=instance.id).delete()
    return JsonResponse({"message": "Deleted"}, status=204)

# End
