from django.shortcuts import render

from .forms import BookingForm

from .models import Doctor
# Create your views here.

#List

def booking_create_view(request):
  form = BookingForm(request.POST or None)
  if form.is_valid():
     form.save()
     form = BookingForm()

  context = {
  'form': form
  }
  return render(request, "booking/booking_create.html", context)


def doctor_detail_view(request):
  obj = Doctor.objects.get(id=1)

  context = {
  'object': obj
  }
  return render(request, "doctor/doctor_detail.html", context)
