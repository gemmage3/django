from django.shortcuts import render

from .models import Doctor
# Create your views here.

#List

def doctor_detail_view(request):
  obj = Doctor.objects.get(id=1)

  context = {
  'object': obj
  }
  return render(request, "doctor/detail.html", context)
