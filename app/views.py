from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie # We import this from the request folder/module so as to get the popular movie from the API
from .models import reviews 
from .forms import ReviewForm  #Imported furing coding for reviews. 

Review = reviews.Review  #Imported during coding for reviews. 

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )


@app.route('/movie/<int:id>') # Update our route to access the id of the movies. 
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id) #We add this when getting reviews and call the
               # .get_reviews() method that takesin the movie ID and returns the list of reviews
    return render_template('movie.html',title = title,movie = movie,reviews = reviews)


@app.route('/search/<movie_name>') 
def search(movie_name):#We create a search view function that has passes in a dynamic variable. 
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)


@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm() #We create an instance of the ReviewForm class and name it form 
    movie = get_movie(id) # to get the movie object for the movie with that ID.

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review) #we gather the data from the form input fields and create a new review object
        new_review.save_review() # to save the created new review object
        return redirect(url_for('movie',id = movie.id )) # redirect the response to the movie view function and pass in the dynamic movie ID.

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)