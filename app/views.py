from django.shortcuts import render

from . models import Doctor
# Create your views here.

#List

def doctor_list_view(request):
  doctor_objects - Doctor.objects.all()

  context = {
  'doctor_objects': doctor_objects

  }
  return render(request, "doctors.html", context)
