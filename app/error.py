#Function to handle an error if a user enters the wrong url.

from flask import render_template # We import the render_template() function
from app import app  # We import the flask application instance.

@app.errorhandler(404)   #We create a new decorator app.errorhandler() that passes in the error we receive.
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404 #We create a view function. that returns fourOwfour.html file and we also pass in the status code we receive 404