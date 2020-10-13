from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from datetime import datetime

# Create your models here.

class Doctor(models.Model):

  name = models.CharField(max_length=30)
  main_img = models.ImageField(blank=True)
  summary = models.TextField(default = "Testing")
  location = models.CharField(max_length=50)
  country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)
  virtual_consultation = models.BooleanField(default=False)
  languages = models.CharField(max_length=50, default=0)
  years_experience = models.PositiveIntegerField(default=0)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0
    )
  price_quote_available = models.BooleanField(default=False)
  procedures = models.ManyToManyField('Procedure')

class Booking(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    CONSULTATION_STATUS = ((BOOKED, 'Booked'),
                            (CANCELLED, 'Cancelled'),)
    doctor_id=models.ForeignKey('Doctor', on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.TimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=CONSULTATION_STATUS, default=BOOKED, max_length=255)
    timestamp = models.DateTimeField(null=True, blank=True)


class Country(models.Model):
  UK = 0
  SPAIN = 1
  TURKEY = 2
  GREECE = 3
  THAILAND = 4
  COLUMBIA = 5
  DOMINICAN_REPUBLIC = 6
  MEXICO = 7
  COSTA_RICA = 8
  BELGIUM = 9
  COUNTRY_CHOICES = (
    (0, 'UK'),
    (1, 'SPAIN'),
    (2, 'TURKEY'),
    (3, 'GREECE'),
    (4, 'THAILAND'),
    (5, 'COLUMBIA'),
    (6, 'DOMINICAN_REPUBLIC'),
    (7, 'MEXICO'),
    (8, 'COSTA_RICA'),
    (9, 'BELGIUM'),
    )
  country_name = models.PositiveIntegerField(choices = COUNTRY_CHOICES,blank=True, default=0
    )

class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=30, blank=False)
    procedure_description = models.TextField(default = "Description", blank=False)




