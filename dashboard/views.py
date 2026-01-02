from django.shortcuts import render
from movies.models import Movie, Theatre, Booking
from payments.models import Payment
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count


@staff_member_required
def admin_dashboard(request):
    total_revenue = (Payment.objects.filter(status="Paid").aggregate(total=Sum('amount'))['total'] or 0)

    popular_movies = (Booking.objects.values('movie__name').annotate(total_bookings=Count('id')).order_by("-total_bookings")[:5])

    busiest_theatres = (Booking.objects.values('theatre__name').annotate(total_bookings=Count('id')).order_by("-total_bookings")[:5])

    total_bookings = Booking.objects.count()

    return render(request, 'dashboard/admin_dashboard.html', {
        'total_revenue': total_revenue,
        'popular_movies': popular_movies,
        'busiest_theatres': busiest_theatres,
        'total_bookings': total_bookings,
    })