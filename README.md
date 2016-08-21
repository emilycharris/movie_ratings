# movie_ratings
Movie Ratings homework using Django

_Create an interface in Django to the MovieLens dataset._

**Objectives**

After completing this assignment, you should be able to:
- Create a new Django application
- Translate real-world data to Django models
- Explain what a database is
- Explain what a model is
- Use the Django admin
- Structure the Django admin to reflect your data
- Create regular expressions to map URLs to views
- Explain what a view is
- Explain what a template is
- Design simple views
- Use basic HTML
- Extrapolate from basic HTML how to create templates
- Distinguish when to use GET vs POST
- Create forms

##Part 1

###Normal Mode

- Download the dataset from the MovieLens dataset options and read its README.
- Create a new Django application called movieratings to hold your models.
- Create Django models for users (call the model Rater so as not to confuse it with Django users), movies, and ratings. Make sure that your models can contain the data from your dataset.
- Create Django admin pages for your models.

###Hard Mode
- Start adding methods to your models that you will need later. For movie, you'll want the average rating for each movie, and the ability to get the top movies by rating.
- For rater, you'll want the average rating that rater gave to a movie, and the ability to get the top movies that rater has not seen. You will also want to be able to find the Euclidean distance between that rater and another using their movie ratings.
- In order to do this, you'll want to read up on the model layer of Django.

##Part 2

###Normal Mode
- Using the datamigration method we went over in class. Load in your fixture data from your datasets into django models.
- In your Django application, create views and templates for:
 - The top 20 movies rated. This list of movies should have their average rating, and each movie listed should have a link to its individual page.
 - Each individual movie. This page should have the movie, its average rating, and each person who rated it. The list of people should have the rating with each person and should have a link to that person's page.
 - Add the ability to create a review for an existing movie.
 - Each individual user. This page should have their demographic data, and a list of all movies they've rated, with the rating they gave it. Each movie listed should have the rating they gave it beside it and should have a link to that movie's page.

In order to complete this assignment, I used Python and Django.
