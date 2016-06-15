import csv
from django.db.models import Avg

def add_movie_data(apps, schema_editor):
    Movie = apps.get_model('movieratings', 'Movie')
    with open('u.movies', encoding='latin1') as infile:
        movie_data = csv.DictReader(infile, delimiter="|", fieldnames=('movie_id','title', 'release_date',
                                                                       'video_release_date', 'imdb_url', 'unknown',
                                                                       'action', 'adventure', 'animation', 'children',
                                                                       'comedy', 'crime', 'documentary', 'drama',
                                                                       'fantasy', 'film_noir', 'horror', 'musical',
                                                                       'mystery', 'romance', 'scifi', 'thriller', 'war',
                                                                       'western'))
        for row in movie_data:
            Movie.objects.create(id=row['movie_id'],
                                 title=row['title'],
                                 release_date=row['release_date'],
                                 video_release_date=row['video_release_date'],
                                 imdb_url=row['imdb_url'],
                                 unknown=row['unknown'],
                                 action=row['action'],
                                 adventure=row['adventure'],
                                 animation=row['animation'],
                                 children=row['children'],
                                 comedy=row['comedy'],
                                 crime=row['crime'],
                                 documentary=row['documentary'],
                                 drama=row['drama'],
                                 fantasy=row['fantasy'],
                                 film_noir=row['film_noir'],
                                 horror=row['horror'],
                                 musical=row['musical'],
                                 mystery=row['mystery'],
                                 romance=row['romance'],
                                 scifi=row['scifi'],
                                 thriller=row['thriller'],
                                 war=row['war'],
                                 western=row['western'])

def add_rater_data(apps, schema_editor):
    Rater = apps.get_model('movieratings', 'Rater')
    with open('u.raters') as infile:
        rater_data = csv.DictReader(infile, delimiter='|', fieldnames=('rater_id', 'age', 'gender', 'occupation', 'zip'))

        for row in rater_data:
            Rater.objects.create(id=row['rater_id'], age=row['age'], gender=row['gender'],
                                 occupation=row['occupation'], zip=row['zip'])


def add_rating_data(apps, schema_editor):
    Rater = apps.get_model('movieratings', 'Rater')
    Movie = apps.get_model('movieratings', 'Movie')
    Rating = apps.get_model('movieratings', "Rating")

    with open('u.ratings') as infile:
        rating_data = csv.DictReader(infile, delimiter='\t', fieldnames=('rater_id', 'movie_id', 'rating', 'timestamp'))
        for row in rating_data:
            movie = Movie.objects.get(id=row['movie_id'])

            rater = Rater.objects.get(id=row['rater_id'])
            Rating.objects.create(movie=movie,
                                  rater=rater,
                                  rating=row['rating'],
                                  timestamp=row['timestamp'])

from django.db.models import Avg, Count


from django.db.models import Avg, Count

def add_avg_rating(apps, schema_editor):
    Movie = apps.get_model('movieratings', 'Movie')
    Rating = apps.get_model('movieratings', "Rating")
    Avg_Rating = apps.get_model('movieratings', 'Avg_Rating')

    movies = Movie.objects.all()

    for movie_item in movies:


        avg_rating_dict = Rating.objects.filter(movie=movie_item
        ).values('rating').aggregate(average_rating=Avg("rating"))

        avg_rating = avg_rating_dict.get('average_rating')

        count_rating_dict = Rating.objects.filter(movie=movie_item
        ).values('rating').aggregate(count_rating=Count('rating'))

        count_rating = count_rating_dict.get('count_rating')

        weighted_avg = avg_rating * (count_rating * .1)
        print(movie_item.title, avg_rating, count_rating, weighted_avg)


        Avg_Rating.objects.create(movie=movie_item,
        count_ratings=count_rating,
        average_rating=avg_rating,
        weighted_averaged=weighted_avg)

    raise Exception("boom")