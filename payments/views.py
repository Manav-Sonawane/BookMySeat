from django.shortcuts import render
from django.conf import settings
from .models import Payment
from .services import create_order
from movies.models import Seat, Booking, Theatre
from django.http import JsonResponse
import json
from movies.utils import send_booking_confirmation
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def verify_payment(request):
    data = request.session.get('booking')

    if not data:
        return JsonResponse({"error": "No booking session"}, status=400)
    
    payload = json.loads(request.body)
    razorpay_order_id = payload.get("razorpay_order_id")
    razorpay_payment_id = payload.get("razorpay_payment_id")
    razorpay_signature = payload.get("razorpay_signature")
    
    booked_seats = []
    theatre = Theatre.objects.get(id=data['theatre_id'])

    with transaction.atomic():
        payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
        payment.razorpay_payment_id = razorpay_payment_id
        payment.razorpay_signature = razorpay_signature
        payment.status = "Paid"
        payment.save()

        seats = Seat.objects.select_for_update().filter(id__in=data["seats_ids"])

        for seat in seats:
            if seat.reserved_by != request.user:
                return JsonResponse({"error": "Seat reservation invalid"}, status=400)
            
            seat.is_booked = True
            seat.reserved_by = None
            seat.reserved_until = None
            seat.save()

            Booking.objects.create(
                user=request.user,
                seat=seat,
                movie_id=data['movie_id'],
                theatre_id=data['theatre_id']
            )

            booked_seats.append(seat.seat_number)
    

    send_booking_confirmation(
        user=request.user,
        seat_numbers=booked_seats,
        theatre=theatre
    )

    del request.session['booking']

    return JsonResponse({'redirect_url': '/profile/'})
