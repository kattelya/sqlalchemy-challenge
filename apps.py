# import flask
# following along from class exercise to build my homework
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np

######### Database Setup #########
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Session (link) from Python to the database
session = Session(engine)

######### Flask Setup #########
# create an app, be sure to pass __name__ (from class exercise)
app = Flask(__name__)


######### Flask Routes #########
# define what to do when a user hits the index route  
# List all routes that are available 
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
        )

# define what to do when a user hits the "name of the page" similar to the home ones 
# route 1 is the list of stations page 
# @app.route("/name of the page")
# def (name of the page)():
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html
# when np.ravel is use the list function need to be implemented - otherwise it throw an error
@app.route("/api/v1.0/stations")
def stations():
    """read our data for list of stations"""
    result = session.query(Station.station).all()
    stations = list(np.ravel(result))
    return jsonify(stations)

# route 2 is query precipitation 
# @app.route("/name of the page")
# def (name of the page)():
@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify()





if __name__ == "__main__":
    app.run(debug=True)