from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Seat

def release_expired_reservations():
    Seat.objects.filter(
        reserved_until__lt=timezone.now(),
        is_booked=False
    ).update(reserved_by=None, reserved_until=None)

def send_booking_confirmation(user, seat_numbers, theatre):
    subject = "Your Movie Booking is Confirmed!"

    message = f"""
    Hi {user.username},

    Your booking is confirmed!

    Movie: {theatre.movie.name}
    Theatre: {theatre.name}
    Show Time: {theatre.time}

    Seats: {", ". join(seat_numbers)}

    Enjoy the show!
    """
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
