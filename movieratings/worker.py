import csv

def add_movie_data(apps, schema_editor):
    with open('u.movies', encoding='latin1') as infile:
        movie_data = csv.DictReader(infile, delimiter="|", fieldnames=('movie_id','title', 'release_date',
                                                                       'video_release_date', 'imdb_url', 'unknown',
                                                                       'action', 'adventure', 'animation', 'children',
                                                                       'comedy', 'crime', 'documentary', 'drama',
                                                                       'fantasy', 'film_noir', 'horror', 'musical',
                                                                       'mystery', 'romance', 'scifi', 'thriller', 'war',
                                                                       'western'))
        Movie = apps.get_model('movieratings', 'Movie')
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
    raise Exception('boom')

