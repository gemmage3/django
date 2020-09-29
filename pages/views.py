from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is my home"
    }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is the about page"
    }
    return render(request, "about.html", my_context)

def doctor_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is the doctor page"
    }
    return render(request, "doctor.html", my_context)

def procedure_view(request, *args, **kwargs):
    my_context = {
      "my_text": "This is the procedure page"
    }
    return render(request, "procedure.html", my_context)

