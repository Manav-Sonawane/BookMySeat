from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'razorpay_order_id',
        'razorpay_payment_id',
        'amount',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('razorpay_order_id', 'razorpay_payment_id')
    ordering = ('-created_at',)
    readonly_fields = (
        'razorpay_order_id',
        'razorpay_payment_id',
        'razorpay_signature',
        'created_at',
    )
