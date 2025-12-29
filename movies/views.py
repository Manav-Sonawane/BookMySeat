from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Theatre, Seat, Booking, Genre, Language
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .utils import send_booking_confirmation

def movie_list(request):
    search_query = request.GET.get('search')
    language = request.GET.get('language')
    selected_genres = request.GET.getlist('genre')

    movies = Movie.objects.all()

    if search_query:
        movies = movies.filter(name__icontains=search_query)

    if language:
        movies = movies.filter(language__name__iexact=language)
    
    if selected_genres:
        movies = movies.filter(genre__name__in=selected_genres)

    movies = movies.distinct()

    return render(request, 'movies/movies_list.html', {
        'movies': movies,
        'genres': Genre.objects.all(),
        'languages': Language.objects.all(),
        'selected_genres': selected_genres,
    })

def theatre_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    theatre = Theatre.objects.filter(movie=movie)

    return render(request, 'movies/theatre_list.html', {
        'movie': movie,
        'theatres': theatre})

@login_required(login_url='/login/')
def booking_seats(request, theatre_id):
    theatre = get_object_or_404(Theatre, id=theatre_id)
    seats = Seat.objects.filter(theatre=theatre,).order_by('seat_number')

    if request.method == 'POST':
        selected_Seats = request.POST.getlist('seats')
        # error_seats=[]
        # booked_seats = []

        if not selected_Seats:
            return render(request, 'movies/seat_selection.html', {'theatre':theatre, 'seats':seats, 'error':'No seat selected'})
        
        unavailable = Seat.objects.filter(
            id__in=selected_Seats,
            is_booked=True
        )

        if unavailable.exists():
            return render(request, 'movies/seat_selection.html',{
                'theatre': theatre,
                'seats': seats,
                'error': 'Some selected seats are already booked.'
            })
        
        request.session['booking'] = {
            'theatre_id': theatre.id,
            'movie_id': theatre.movie.id,
            'seats_ids': selected_Seats,
            'seat_count': len(selected_Seats)
        }

        return redirect('movies:confirm_booking')
    
    return render(request, 'movies/seat_selection.html', {
        'theatre': theatre,
        'seats': seats
    })
        # for seat_id in selected_Seats:
        #     seat = get_object_or_404(Seat, id=seat_id, theatre=theatre)

        #     if seat.is_booked:
        #         error_seats.append(seat.seat_number)
        #         continue

        #     try:
                # Booking.objects.create(
                #     user=request.user,
                #     seat=seat,
                #     movie=theatre.movie,
                #     theatre=theatre
                # )
                # seat.is_booked = True
                # seat.save()
            #     booked_seats.append(seat.seat_number)

            # except IntegrityError:
            #     error_seats.append(seat.seat_number)

        # if error_seats:
        #     error_message = f'The follwoing seat is already booked: {",".join(error_seats)}'
        #     return render(request, 'movies/seat_selection.html', {'theatre':theatre, 'seats':seats, 'error':error_message})
        
        # if booked_seats:
            # send_booking_confirmation(request.user, booked_seats, theatre)

        # return redirect('profile')
    # return render(request, 'movies/seat_selection.html', {'theatre': theatre, 'seats': seats})

@login_required
def confirm_booking(request):
    data = request.session.get('booking')

    if not data:
        return redirect('movies:movie_list')
    
    theatre = get_object_or_404(Theatre, id=data['theatre_id'])
    seat_price = theatre.seat_price
    total_amount = seat_price * data['seat_count']

    return redirect(
        'payments:start-payment',
        theatre_id=theatre.id,
        amount=total_amount
    )