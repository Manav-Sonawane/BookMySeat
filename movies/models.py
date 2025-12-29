from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="movies/")
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    cast=models.TextField()
    description=models.TextField(blank=True,null=True)

    trailer_url=models.URLField(blank=True, null=True)

    genre=models.ManyToManyField(Genre, related_name='mvoies')
    language=models.ForeignKey(Language, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.name
    
class Theatre(models.Model):
    name=models.CharField(max_length=255)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='theatres')
    time=models.DateTimeField()
    seat_price=models.IntegerField(default=499, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.movie.name} - {self.time}"
    
class Seat(models.Model):
    theatre=models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='seats')
    seat_number=models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.seat_number} in {self.theatre.name}'
    
class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    seat=models.OneToOneField(Seat, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookings')
    theatre=models.ForeignKey(Theatre, on_delete=models.CASCADE)
    booked_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking by{self.user.username} for {self.seat.seat_number} at {self.theatre.name}'