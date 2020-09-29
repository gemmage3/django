from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    (4, 'Chinese')
    )

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  address = models.TextField(default = "Testing")
  county = models.ForeignKey('Country', on_delete=models.CASCADE, default=0)
  virtual_consultation = models.BooleanField(default=False)
  languages = models.PositiveIntegerField(choices = LANGUAGE_CHOICES,blank=True, default=0
    )
  rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0
    )
  price_quote_available = models.BooleanField(default=False)


class Country(models.Model):
  country_name = models.CharField(max_length=30)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    CONSULTATION_STATUS = ((BOOKED, 'Booked'),
                            (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    user_id =models.ForeignKey('User', on_delete=models.CASCADE, default=0)
    doctor_id=models.ForeignKey('Doctor', on_delete=models.CASCADE, default=0)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=CONSULTATION_STATUS, default=BOOKED, max_length=255)


