# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 19:34
from __future__ import unicode_literals

from django.db import migrations

from django.db.models import Avg, Count
from movieratings.models import Avg_Rating

def add_avg_rating(apps, schema_editor):
    Movie = apps.get_model('movieratings', 'Movie')
    Rating = apps.get_model('movieratings', "Rating")

    movies = Movie.objects.all()

    for movie_item in movies:


        avg_rating_dict = Rating.objects.filter(movie=movie_item
        ).values('rating').aggregate(average_rating=Avg("rating"))
        avg_rating = avg_rating_dict.get('average_rating')

        count_rating_dict = Rating.objects.filter(movie=movie_item
        ).values('rating').aggregate(count_rating=Count('rating'))
        count_rating = count_rating_dict.get('count_rating')

        print(movie_item.title, avg_rating, count_rating)
        #Avg_Rating.objects.create(movie=movie_item,
        #count_ratings=count_rating,
        #average_rating=avg_rating)

    raise Exception("boom")



class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0005_auto_20160611_1913'),
    ]

    operations = [
        migrations.RunPython(add_avg_rating)
    ]
