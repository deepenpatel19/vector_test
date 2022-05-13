from django.http import JsonResponse
from django.db.models import Sum
from .models import Continent, Country, City


def city_area_and_population_validator(function):
    """
    Validate area and population of city is less than country.
    """
    def _function(request, *args, **kwargs):
        # print(f"city area and population decorator {request} {args} {kwargs}")

        validation_errors = []

        id = kwargs.get("pk", "")
        total_country_area = 0
        total_country_population = 0

        total_city_area = 0
        city_current_area_to_deduct = 0
        total_city_population = 0
        city_current_population_to_deduct = 0

        if id:
            country_query = Country.objects.filter(city__id=id).annotate(
                total_population=Sum("population")).annotate(total_area=Sum("area")).first()
            city_query = Country.objects.filter(city__id=id).annotate(total_city_population=Sum(
                "city__population")).annotate(total_city_area=Sum("city__area")).first()
            city_object = City.objects.filter(id=id).first()
            city_current_area_to_deduct = city_object.area
            city_current_population_to_deduct = city_object.population
        else:
            country_query = Country.objects.filter(id=request.data.get(
                "country", "")).annotate(total_population=Sum("population")).annotate(total_area=Sum("area")).first()
            city_query = Country.objects.filter(id=request.data.get(
                "country", "")).annotate(total_city_population=Sum("city__population")).annotate(total_city_area=Sum("city__area")).first()

        if country_query and city_query:
            total_country_area = country_query.total_area
            total_country_population = country_query.total_population
            total_city_area = city_query.total_city_area if city_query.total_city_area else 0
            total_city_area = total_city_area - city_current_area_to_deduct
            total_city_population = city_query.total_city_population if city_query.total_city_population else 0
            total_city_population = total_city_population - city_current_population_to_deduct

            # print(f"city: total area {total_country_area} {total_city_area} {city_current_area_to_deduct}")
            # print(
            # f"city: total population {total_country_population} {total_city_population} {city_current_population_to_deduct}")
        else:
            return JsonResponse(
                {
                    "message": "Data not found."
                },
                status=400
            )

        try:
            if request.data.get("area", "") and not total_country_area >= total_city_area + float(request.data.get("area", "")):
                validation_errors.append("Area should be less than or equal to total area of the Country.")
                # return JsonResponse({"message": "Area should be less than or equal to total area of the Country."}, status=400)
        except ValueError as e:
            # print(f"city: area validation error {e}")
            validation_errors.append("Conversion Error for value of `area` parameter.")
            # return JsonResponse({"message": "Conversion Error for value of `area` parameter."}, status=400)

        try:
            if request.data.get("population", "") and not total_country_population >= total_city_population + float(request.data.get("population", "")):
                validation_errors.append("Population should be less than or equal to total population of the Country.")
                # return JsonResponse({"message": "Area should be less than or equal to total area of the Country."}, status=400)
        except ValueError as e:
            # print(f"city: area validation error {e}")
            validation_errors.append("Conversion Error for value of `population` parameter.")
            # return JsonResponse({"message": "Conversion Error for value of `area` parameter."}, status=400)

        if validation_errors:
            return JsonResponse(
                {
                    "message": validation_errors
                },
                status=400
            )

        return function(request, *args, **kwargs)

    return _function


def country_area_and_population_validator(function):
    """
    Validate area and population of country is less than continent.
    """
    def _function(request, *args, **kwargs):
        # print(f"country area and population decorator {request} {request.data} {args} {kwargs}")

        validation_errors = []

        id = kwargs.get("pk", "")

        total_continent_area = 0
        total_continent_population = 0

        total_country_area = 0
        country_current_area_to_deduct = 0
        total_country_population = 0
        country_current_population_to_deduct = 0

        if id:
            continent_query = Continent.objects.filter(country__id=id).annotate(
                total_population=Sum("population")).annotate(total_area=Sum("area")).first()
            country_query = Continent.objects.filter(country__id=id).annotate(total_country_population=Sum(
                "country__population")).annotate(total_country_area=Sum("country__area")).first()
            country_object = Country.objects.filter(id=id).first()
            country_current_area_to_deduct = country_object.area
            country_current_population_to_deduct = country_object.population
        else:
            continent_query = Continent.objects.filter(id=request.data.get("continent", "")).annotate(
                total_population=Sum("population")).annotate(total_area=Sum("area")).first()
            country_query = Continent.objects.filter(id=request.data.get("continent", "")).annotate(total_country_population=Sum(
                "country__population")).annotate(total_country_area=Sum("country__area")).first()

        if continent_query and country_query:
            total_continent_area = continent_query.total_area
            total_continent_population = continent_query.total_population
            total_country_area = country_query.total_country_area if country_query.total_country_area else 0
            total_country_area = total_country_area - country_current_area_to_deduct
            total_country_population = country_query.total_country_population if country_query.total_country_population else 0
            total_country_population = total_country_population - country_current_population_to_deduct
        else:
            return JsonResponse(
                {
                    "message": "Data not found."
                },
                status=400
            )

            # print(f"country: total area {total_continent_area} {total_country_area} {country_current_area_to_deduct}")
            # print(
            #     f"country: total population {total_continent_population} {total_country_population} {country_current_population_to_deduct}")

        try:
            if request.data.get("area", "") and not(total_continent_area >= total_country_area + float(request.data.get("area", ""))):
                validation_errors.append("Area should be less than or equal to total area of the Continent.")
                # return JsonResponse({"message": "Area should be less than or equal to total area of the Country."}, status=400)
        except ValueError as e:
            # print(f"country: area validation error {e}")
            validation_errors.append("Conversion Error for value of `area` parameter.")
            # return JsonResponse({"message": "Conversion Error for value of `area` parameter."}, status=400)

        try:
            if request.data.get("population", "") and not(total_continent_population >= total_country_population + int(request.data.get("population", ""))):
                validation_errors.append(
                    "Population should be less than or equal to total population of the Continent.")
                # return JsonResponse({"message": "Area should be less than or equal to total area of the Country."}, status=400)
        except ValueError as e:
            # print(f"country: area validation error {e}")
            validation_errors.append("Conversion Error for value of `population` parameter.")
            # return JsonResponse({"message": "Conversion Error for value of `area` parameter."}, status=400)

        if validation_errors:
            return JsonResponse(
                {
                    "message": validation_errors
                },
                status=400
            )

        return function(request, *args, **kwargs)

    return _function
