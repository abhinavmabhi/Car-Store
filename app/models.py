from django.db import models
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile
import os


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Car_Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fuel_Type(models.Model):
    fuel_choices = (
        ("Petrol", "Petrol"),
        ("Diesel", "Diesel"),
        ("Electric", "Electric"),
        ("Hybrid", "Hybrid"),
        ("Semi-Automatic", "Semi-Automatic"),
        ("CVT", "CVT"),
        ("Dual-Clutch", "Dual-Clutch"),
        ("AMT", "AMT"),
    )

class Transmission_Type(models.Model):
    transmission_choices = (
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
    )

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="Brand")
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Car_Type, on_delete=models.CASCADE, related_name="Car_type")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="Model")
    fuel_type = models.CharField(max_length=100, choices=Fuel_Type.fuel_choices)
    transmission = models.CharField(max_length=100, choices=Transmission_Type.transmission_choices)
    year = models.IntegerField()
    total_km_run = models.PositiveIntegerField(help_text="Total distance driven (in km)")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    mileage = models.FloatField(help_text="Mileage in km/l or km per charge")
    color = models.CharField(max_length=50)
    owner_count = models.IntegerField(default=1, help_text="Number of previous owners")
    image = models.ImageField(upload_to="car_image")

    image1 = models.ImageField(upload_to="car_image", blank=True, null=True)
    image2 = models.ImageField(upload_to="car_image", blank=True, null=True)
    image3 = models.ImageField(upload_to="car_image", blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} {self.model.name} ({self.year})"
