from django.db import models
from django.contrib.auth.models import User
from movies.models import Theatre

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default='Created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.razorpay_order_id}"