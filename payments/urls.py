from django.urls import path
from . import views

app_name = "payments"   # 👈 THIS LINE FIXES IT

urlpatterns = [
    path(
        "start/<int:theatre_id>/<int:amount>/",
        views.start_payment,
        name="start-payment"
    ),
    path("verify/", views.verify_payment, name="verify-payment"),
]
