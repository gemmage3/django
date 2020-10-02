from django.shortcuts import render

from .forms import BookingForm, RawBookingForm

from .models import Doctor
# Create your views here.


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
