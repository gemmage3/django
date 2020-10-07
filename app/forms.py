from django import forms

from .models import Booking
from .models import Doctor

class DoctorCreateForm(forms.ModelForm):
  title       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
  summary     = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Summary",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )

  class Meta:
    model = Doctor
    fields = ['name',
        'main_img',
        'summary',
        'location',
        'country',
        'virtual_consultation',
        'languages',
        'years_experience',
        'price_quote_available',
        'procedures']

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



