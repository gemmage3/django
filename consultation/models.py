from django.db import models

# Create your models here.

class Doctor(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  address = models.CharField(max_length=150, blank=True, null=True)
  virtual_consultation = models.BooleanField()
  years_experience = models.IntegerField()
  languages = models.CharField(max_length=30, blank=True, null=True)
  price_quote = models.BooleanField()

