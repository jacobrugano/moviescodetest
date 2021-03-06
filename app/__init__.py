from flask import Flask
from .config import DevConfig #To make our application use the new configurations
from flask_bootstrap import Bootstrap



# Initializing application
app = Flask(__name__,instance_relative_config = True) #We have passed in the instance to allow us to connect to the instance folder

#Setting up configuration
app.config.from_object(DevConfig) #We use this to set up the configurations and pass in the DevConfig subclass
app.config.from_pyfile('config.py') #conects us to the config file and we append all its content to the app.config


# Initializing Flask Extensions////This is how most Extensions are initialized.
bootstrap = Bootstrap(app)

from app import views
from app import error