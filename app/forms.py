from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):

  class Meta:
    model = Booking
    fields = ['price',
              'date',
              'time']

class RawBookingForm(forms.Form):
  price = forms.DecimalField()
  date = forms.DateField()
  time = forms.TimeField()



