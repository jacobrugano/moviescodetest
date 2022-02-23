from flask import render_template
from app import app
from .request import get_movies # We import this from the request folder/module so as to get the popular movie from the API

# Viewss
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
#Getting popular movie
    popular_movies = get_movies('popular') #We get the most popular movies and store them in a variable...and we have to pass in the popular as an argument.
    # print(popular_movies)
    upcoming_movie = get_movies('upcoming')  #We get the upcoming movies and store them in a variable...and we have to pass in the upcoming as an argument.
    now_showing_movie = get_movies('now_playing')  #We get the current movies and store them in a variable...and we have to pass in the now_playing as an argument.
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie) #We pass the result to our template


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = f'You are viewing {movie_id}'
    return render_template('movie.html',id = movie_id, title = title)

