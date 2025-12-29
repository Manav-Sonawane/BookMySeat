import razorpay
from django.conf import settings

client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)

def create_order(amount):
    return client.order.create({
        "amount": amount * 100,  # rupees → paise
        "currency": "INR",
        "payment_capture": 1
    })
