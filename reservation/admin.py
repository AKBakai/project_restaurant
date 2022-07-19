from django.contrib import admin

from reservation.models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'number_of_number',
        'date',
        'time'
    )