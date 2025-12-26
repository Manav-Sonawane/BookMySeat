from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Theatre, Seat, Booking, Genre, Language
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

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

    return render(request, 'movies/movies_list.html', {'movies': movies, 'genres': Genre.objects.all(), 'languages': Language.objects.all(), 'selected_genres': selected_genres})

def theatre_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    theatre = Theatre.objects.filter(movie=movie)

    return render(request, 'movies/theatre_list.html', {'movie': movie, 'theatres': theatre})

@login_required(login_url='/login/')
def booking_seats(request, theatre_id):
    theatre = get_object_or_404(Theatre, id=theatre_id)
    seats = Seat.objects.filter(theatre=theatre, is_booked=False)
    if request.method == 'POST':
        selected_Seats = request.POST.getlist('seats')
        error_seats=[]
        if not selected_Seats:
            return render(request, 'movies/seat_selection.html', {'theatre':theatre, 'seats':seats, 'error':'No seat selected'})
        for seat_id in selected_Seats:
            seat = get_object_or_404(Seat, id=seat_id, theatre=theatre)
            if seat.is_booked:
                error_seats.append(seat.seat_number)
                continue
            try:
                Booking.objects.create(
                    user=request.user,
                    seat=seat,
                    movie=theatre.movie,
                    theatre=theatre
                )
                seat.is_booked = True
                seat.save()
            except IntegrityError:
                error_seats.append(seat.seat_number)
        if error_seats:
            error_message = f'The follwoing seat is already booked: {",".join(error_seats)}'
            return render(request, 'movies/seat_selection.html', {'theatre':theatre, 'seats':seats, 'error':error_message})
        return redirect('profile')
    return render(request, 'movies/seat_selection.html', {'theatre': theatre, 'seats': seats})

