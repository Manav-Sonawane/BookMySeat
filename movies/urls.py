from django.contrib.auth import views as auth_views
from django.urls import path
from .views import movie_list, theatre_list, booking_seats

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:movie_id>/theatres/', theatre_list, name='theatre_list'),
    path('theatre/<int:theatre_id>/seats/book/', booking_seats, name='seat_list'),
]