from django.db import models

# Create your models here.
import csv

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=12)
    video_release_date = models.CharField(max_length=12)
    imdb_url = models.CharField(max_length=300)
    unknown = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    scifi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.rating)

class Avg_Rating(models.Model):
    movie = models.ForeignKey(Movie)
    count_ratings = models.IntegerField()
    average_rating = models.FloatField()

    def __str__(self):
        return str(self.average_rating)

    @property
    def sorted_set(self):
        return self.average_rating.order_by('average_rating')




