from django.shortcuts import render
from django.conf import settings
from .models import Payment
from .services import create_order
from movies.models import Seat, Booking, Theatre
from django.http import JsonResponse
import json
from movies.utils import send_booking_confirmation

def start_payment(request, theatre_id, amount):
    order = create_order(amount)

    Payment.objects.create(
        user=request.user,
        theatre_id=theatre_id,
        amount=amount,
        razorpay_order_id=order["id"]
    )

    return render(request, "payments/checkout.html", {
        "order_id": order["id"],
        "amount": amount * 100,  # Razorpay uses paise
        "key": settings.RAZOR_KEY_ID
    })


def verify_payment(request):
    data = request.session.get('booking')

    if not data:
        return JsonResponse({"error": "No booking session"}, status=400)

    booked_seats = []
    theatre = Theatre.objects.get(id=data['theatre_id'])

    for seat_id in data['seats_ids']:
        seat = Seat.objects.get(id=seat_id)
        Booking.objects.create(
            user=request.user,
            seat=seat,
            movie_id=data['movie_id'],
            theatre_id=data['theatre_id']
        )
        seat.is_booked = True
        seat.save()

        booked_seats.append(seat.seat_number)

    send_booking_confirmation(
        user=request.user,
        seat_numbers=booked_seats,
        theatre=theatre
    )

    del request.session['booking']

    return JsonResponse({'redirect_url': '/profile/'})
