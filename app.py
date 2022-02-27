import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Use create_engine() to access and query SQLite database file:
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes:
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save our references to each table:
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database:
session = Session(engine)

# Create a Flask application called "app":
app = Flask(__name__)

# Define the welcome route:
@app.route("/")

# Create a function welcome() with a return statement,
# then add the precipitation, stations, tobs, and temp routes:
def welcome():
    return
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


