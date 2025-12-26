from django.contrib import admin
from .models import Movie, Theatre, Seat, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'cast', 'description']

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie', 'time']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theatre', 'seat_number', 'is_booked']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'seat', 'movie', 'theatre', 'booked_at']