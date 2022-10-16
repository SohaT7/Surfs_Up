# Import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependency
from flask import Flask, jsonify

# Use create_engine() to access and query SQLite database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into the classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table, i.e. create variables for the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# Create a Flask application called "app"
app = Flask(__name__)


# In case app.py needs to be imported to another Python file named example.py
# Use magic method __name__ to check file source of running code
# import app
# print("example __name__ = %s", __name__)
# if __name__ == "__main__":
    # print("example is being run directly.")
# else:
    # print("example is being imported")


# Define the starting point, i.e. the root
@app.route("/")

# Add the routing information for each of the other routes to a welcome() function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! \n
    Available Routes: \n
    /api/v1.0/precipitation \n
    /api/v1.0/stations \n
    /api/v1.0/tobs \n
    /api/v1.0/temp/start/end \n
    ''')


# Create precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
def precipitation():
    # Calculate the date one year ago from the last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query to get date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    # Create a dictionary for the results
    precip = {date: prcp for date, prcp in precipitation}
    
    # Format the result into a JSON structured file
    return jsonify(precip)


# Create stations route
@app.route("/api/v1.0/stations")

# Create the stations() function
def stations():
    # Query to get all of the stations in the database
    results = session.query(Station.station).all()
    
    # Unravel 'results' into a one-dimensional array 
    # Then convert 'results' array into a list
    stations = list(np.ravel(results))
    
    # Format the results into a JSON structured file
    return jsonify(stations=stations) 


# Create the temperature observations route
@app.route("/api/v1.0/tobs")

# Create the temp_monthly() function
def temp_monthly():
    # Calculate the date one year ago from the last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query the primary station for all temperature observations from previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # Unravel 'results' into a 1D array, and the array into a list
    temps = list(np.ravel(results))
    
    # Format the results into a JSON structured file
    return jsonify(temps=temps)


# Create the statistics route
# Add the starting date
@app.route("/api/v1.0/temp/<start>")
# Add the ending date
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the stats() function
def stats(start=None, end=None):
    # Create a list called 'sel' which determines the data points to be collected by the query
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Add an 'if-not` statement to determine the start and end date
    if not end:
        # Query to get data points in 'sel' list based on start date
            # *sel to indicate there will be multiple results for the query
            results = session.query(*sel).\
                filter(Measurement.date >= start).all()
            # Unravel the 'results' into a 1D array, and the array into a list
            temps = list(np.ravel(results))
            # Format the results into a JSON structured file
            return jsonify(temps)
    
    # Query to get data points in 'sel' list based on start and end dates
    results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    # Unravel the 'results' into a 1D array, and the array into a list
    temps = list(np.ravel(results))
    # Format the results into a JSON structured file
    return jsonify(temps)
 
    