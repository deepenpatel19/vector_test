from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .tasks import *


class ContinentViewSet(viewsets.ViewSet):
    """
    This will provide HTTP methods for different operations for Continents.
    """

    page_size = 10

    def list(self, request, *args, **kwargs):
        return list_continent(request=request, page_size=self.page_size)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of continent'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of continent.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of continent.'),
        }
    ))
    def create(self, request, *args, **kwargs):
        return create_continent(request=request)

    def retrieve(self, request, *args, **kwargs):
        print(f"request {request} {args} {kwargs}")
        return retrieve_continent(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of continent'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of continent.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of continent.'),
        }
    ))
    def update(self, request, *args, **kwargs):
        return update_continent(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of continent'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of continent.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of continent.'),
        }
    ))
    def partial_update(self, request, *args, **kwargs):
        return partial_update_continent(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    def destroy(self, request, *args, **kwargs):
        return delete_continent(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))


class CountryViewSet(viewsets.ViewSet):
    """
    This will provide HTTP methods for different operations for Country.
    """

    page_size = 10

    def list(self, request, *args, **kwargs):
        return list_country(request=request, page_size=self.page_size)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of country'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of country.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of country.'),
            'continent': openapi.Schema(type=openapi.TYPE_STRING, description='Continent ID.'),
            'hospitals': openapi.Schema(type=openapi.TYPE_STRING, description='Number of hospitals.'),
            'national_parks': openapi.Schema(type=openapi.TYPE_STRING, description='Number of national parks.'),
        }
    ))
    def create(self, request, *args, **kwargs):
        return create_country(request=request)

    def retrieve(self, request, *args, **kwargs):
        return retrieve_country(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of country'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of country.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of country.'),
            'continent': openapi.Schema(type=openapi.TYPE_STRING, description='Continent ID.'),
            'hospitals': openapi.Schema(type=openapi.TYPE_STRING, description='Number of hospitals.'),
            'national_parks': openapi.Schema(type=openapi.TYPE_STRING, description='Number of national parks.'),
        }
    ))
    def update(self, request, *args, **kwargs):
        return update_country(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of country'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of country.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of country.'),
            'continent': openapi.Schema(type=openapi.TYPE_STRING, description='Continent ID.'),
            'hospitals': openapi.Schema(type=openapi.TYPE_STRING, description='Number of hospitals.'),
            'national_parks': openapi.Schema(type=openapi.TYPE_STRING, description='Number of national parks.'),
        }
    ))
    def partial_update(self, request, *args, **kwargs):
        return partial_update_country(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    def destroy(self, request, *args, **kwargs):
        return delete_country(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))


class CityViewSet(viewsets.ViewSet):
    """
    This will provide HTTP methods for different operations for City.
    """

    page_size = 10

    def list(self, request, *args, **kwargs):
        return list_city(request=request, page_size=self.page_size)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of city'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of city.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of city.'),
            'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country ID.'),
            'roads': openapi.Schema(type=openapi.TYPE_STRING, description='Number of roads.'),
            'trees': openapi.Schema(type=openapi.TYPE_STRING, description='Number of trees.'),
        }
    ))
    def create(self, request, *args, **kwargs):
        return create_city(request=request)

    def retrieve(self, request, *args, **kwargs):
        return retrieve_city(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of city'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of city.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of city.'),
            'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country ID.'),
            'roads': openapi.Schema(type=openapi.TYPE_STRING, description='Number of roads.'),
            'trees': openapi.Schema(type=openapi.TYPE_STRING, description='Number of trees.'),
        }
    ))
    def update(self, request, *args, **kwargs):
        return update_city(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of city'),
            'population': openapi.Schema(type=openapi.TYPE_STRING, description='Population of city.'),
            'area': openapi.Schema(type=openapi.TYPE_STRING, description='Area in sq meter of city.'),
            'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country ID.'),
            'roads': openapi.Schema(type=openapi.TYPE_STRING, description='Number of roads.'),
            'trees': openapi.Schema(type=openapi.TYPE_STRING, description='Number of trees.'),
        }
    ))
    def partial_update(self, request, *args, **kwargs):
        return partial_update_city(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))

    def destroy(self, request, *args, **kwargs):
        return delete_city(request=request, args=args, kwargs=kwargs, pk=kwargs.get("pk", ""))
