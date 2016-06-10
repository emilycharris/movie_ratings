from django.shortcuts import render

# Create your views here.
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating

def top_20_view(request):
    pass

def movie_view(request, movie_id):
    context = {
        "movies": (Movie.objects.filter(id=movie_id))
    }
    return render(request, "movies.html", context)

def rater_view(request, rater_id):
    context = {
        "raters": (Rater.objects.filter(id=rater_id)),
        "ratings": (Rating.objects.filter(rater=rater_id))
    }
    return render(request, 'raters.html', context)

