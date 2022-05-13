from django.db import models


class Continent(models.Model):
    """
    Details of continent.
    """
    name = models.CharField(max_length=50, default="", unique=True)
    population = models.IntegerField(default=0)
    area = models.FloatField(default=0)  # In sq. meters


class Country(models.Model):
    """
    Details of country.
    """
    name = models.CharField(max_length=50, default="", unique=True)
    continent = models.ForeignKey(Continent, related_name="country", on_delete=models.CASCADE, null=True)
    population = models.IntegerField(default=0)
    area = models.FloatField(default=0)  # In sq. meters
    hospitals = models.IntegerField(default=0)
    national_parks = models.IntegerField(default=0)


class City(models.Model):
    """
    Details of city.
    """
    name = models.CharField(max_length=50, default="")
    country = models.ForeignKey(Country, related_name="city", on_delete=models.CASCADE, null=True)
    population = models.IntegerField(default=0)
    area = models.FloatField(default=0)  # In sq. meters
    roads = models.IntegerField(default=0)
    trees = models.IntegerField(default=0)
