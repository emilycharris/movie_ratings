from django.contrib import admin

# Register your models here.
from movieratings.models import Movie, Rater, Rating

admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Movie)
