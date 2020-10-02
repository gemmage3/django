from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from datetime import datetime

# Create your models here.

class Doctor(models.Model):
  ENGLISH = 0
  SPANISH = 1
  FRENCH = 2
  GERMAN = 3
  CHINESE = 4
  LANGUAGE_CHOICES = (
    (0, 'English'),
    (1, 'Spanish'),
    (2, 'French'),
    (3, 'German'),
    (4, 'Chinese'),
    (5, 'Turkish'),
    (6, 'Russian'),
    (7, 'Arabic'),
    (8, 'Punjabi'),
    (9, 'Japanese')
    )

  name = models.CharField(max_length=30)
  main_img = models.ImageField(blank=True)
  summary = models.TextField(default = "Testing")
  Location = models.CharField(max_length=50)
  country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)
  virtual_consultation = models.BooleanField(default=False)
  languages = models.PositiveIntegerField(choices = LANGUAGE_CHOICES,blank=True, default=0
    )
  years_experience = models.PositiveIntegerField(default=0)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0
    )
  price_quote_available = models.BooleanField(default=False)
  procedures = models.ManyToManyField('Procedure')



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

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Booking(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    CONSULTATION_STATUS = ((BOOKED, 'Booked'),
                            (CANCELLED, 'Cancelled'),)
    user_id =models.ForeignKey('User', on_delete=models.CASCADE, default=0)
    doctor_id=models.ForeignKey('Doctor', on_delete=models.CASCADE, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.TimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=CONSULTATION_STATUS, default=BOOKED, max_length=255)

class Procedure(models.Model):
    PROCEDURE_CHOICES = (
      ('BBL', 'BBL'),
      ('BA', 'BREAST AUGMENTATION'),
      ('RHP', 'RHINOPLASTY'),
      )

    procedure_id = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=30, choices=PROCEDURE_CHOICES, blank=False)
    Procedure_description = models.TextField(default = "Description", blank=False)
    doctors = models.ManyToManyField(Doctor)



