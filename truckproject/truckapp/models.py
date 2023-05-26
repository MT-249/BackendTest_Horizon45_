from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    language_of_profession = models.ForeignKey('Languages', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Truck(models.Model):
    number_plate = models.CharField(max_length=100, unique=True)
    truck_registration_number = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.number_plate


class Languages(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class District(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district
