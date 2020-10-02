from django.contrib import admin

# Register your models here.
from .models import Doctor
from .models import Booking
from .models import Procedure
from .models import Country


admin.site.register(Doctor)
admin.site.register(Booking)
admin.site.register(Procedure)
admin.site.register(Country)
