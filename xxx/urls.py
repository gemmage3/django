"""xxx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from app.views import doctor_detail_view, doctor_list_view, booking_create_view, booking_delete_view, procedure_detail_view, procedure_list_view, procedure_detail_view, country_list_view, country_detail_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('doctor/', doctor_detail_view, name='doctor'),
    path('doctorlist/', doctor_list_view, name='doctor list'),
    path('booking/', booking_create_view, name='booking'),
    path('bookingdelete/', booking_delete_view, name='booking delete'),
    path('procedure/', procedure_detail_view, name='procedure'),
    path('procedurelist/', procedure_list_view, name='procedure list'),
    path('country/', country_detail_view, name='country'),
    path('countrylist/', country_list_view, name='country list'),



    path('admin/', admin.site.urls),
]
