from app import app # To import the app instance
import urllib.request,json # module to help us create a connection to the API URL and send a request .....s
from .models import movie

Movie = movie.Movie

# Getting api key from the config object
api_key = app.config['MOVIE_API_KEY']   # To get the API key

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"] # To get the movie URL



def get_movies(category):    # We create get_movies function that takes movie category as an argument.
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key) #To replace {} placeholders in the base_url with the movie category and the API
            # That creates get_movies_url as thef inal URL for our API request
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read() # The .read() is here to read the response and store it in variable
        get_movies_response = json.loads(get_movies_data) # To check if the response contains any data

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results


def get_movie(id): #created a GET_MOVIE() funtion that takes in the movie ID and returns the movie object.
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object


def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
                                                #We introduce a new URL for our search request that passes in our API key and the 
                                                #movie name then we create the request and process the results.
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results

    
# A function to process the results and Create movie objects.
def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []  # We create this array where we will store our newly created movie objects.
    for movie_item in movie_list:
        id = movie_item.get('id')   # We then use the .GET() method to loop through the list of dictionaries.
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

