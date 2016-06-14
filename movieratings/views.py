from django.shortcuts import render

# Create your views here.
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating
from movieratings.models import Avg_Rating


def top_20_view(request):
    context = {
        "average_rating": (Avg_Rating.objects.all().order_by('-average_rating')[:20]),
    }
    return render(request, 'top_20.html', context)




def movie_view(request, movie_id):
    context = {
        "movies": (Movie.objects.filter(id=movie_id)),
        "ratings": (Rating.objects.filter(movie=movie_id)),
        "average_ratings": (Avg_Rating.objects.filter(movie=movie_id))
    }
    return render(request, "movies.html", context)




def rater_view(request, rater_id):
    context = {
        "raters": (Rater.objects.filter(id=rater_id)),
        "ratings": (Rating.objects.filter(rater=rater_id))
    }
    return render(request, 'raters.html', context)
