from django.contrib import admin
from .models import Movie, Theatre, Seat, Booking, Language, Genre

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'cast', 'description']
    list_filter = ['language', 'genre']
    search_fields = ['name',]
    filter_horizontal = ('genre',)

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie', 'time']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theatre', 'seat_number', 'is_booked']
    list_filter = ['theatre', 'is_booked']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'seat', 'movie', 'theatre', 'booked_at']