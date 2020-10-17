from django.shortcuts import render
from django.http import Http404

from .forms import BookingForm, RawBookingForm, DoctorCreateForm

from .models import Doctor, Procedure

# DOCTOR

def doctor_create_view(request):
      form = DoctorCreateForm(request.POST or None)
      if form.is_valid():
          form.save()


  return render(request, "forms.html", "form":form)

def doctor_detail_view(request, pk):
  try:
      obj = Doctor.objects.get(pk=pk)
  except Doctor.DoesNotExist:
      raise Http404

  context = {
  'object': obj
  }
  return render(request, "doctor/doctor_detail.html", context)

def doctor_list_view(request, *args, **kwargs):
    qs = Doctor.objects.all()
    context = { "object_list": qs}
    return render(request, "doctor/doctor_list.html", context)

# BOOKING

def booking_create_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
       form.save()
       form = BookingForm()

    context = {
    'form': form
    }
    return render(request, "booking/booking_create.html", context)

def booking_delete_view(request, *args, **kwargs):
    my_context = {
      "my_text": "Delete Booking",
      "my_number": "123",
    }
    return render(request, "booking/booking_delete.html", my_context)


# def booking_create_view(request):
#     my_form = RawBookingForm()
#     if request.method =="POST":
#       my_form = RawBookingForm(request.POST)
#     if my_form.is_valid():
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)

#       context = {"form" :my_form}

# return render(request, "booking/booking_create.html", context)

# def booking_create_view(request):

#   my_new_title = request.POST.get('title')

#   context = {}
#   return render(request, "booking/booking_create.html", context)

# PROCEDURE

def procedure_detail_view(request, pk):
    obj = Procedure.objects.get(pk=1)

    context = {
    'object': obj
    }

    return render(request, "procedure/procedure_detail.html", context)

def procedure_list_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is the procedure list page",
      "my_number": "123",
    }
    return render(request, "procedure/procedure_list.html", my_context)

# COUNTRY

def country_detail_view(request, pk, *args, **kwargs):

    obj = Country.objects.get(pk=1)

    context = {
    'object': obj
    }

    return render(request, "country/country_detail.html", context)

def country_list_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is the country list page"
    }
    return render(request, "country/country_list.html", my_context)


