# import flask
# following along from class exercise to build my homework
from flask import Flask, jsonify

# create an app, be sure to pass __name__ (from class exercise)
app = Flask(__name__)

hello_dict = {"Hello": "world!"}

# define what to do when a user hits the index route  
@app.route("/")
def home():
    print ("hello world")
    return ("Welcome")

# define what to do when a user hits the "name of the page" similar to the home ones 
# @app.route("/name of the page")
# def (name of the page)():

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


#####################
# Create your dictionary 
# justice_league_members = [{ a: 1, b: 2}, {c:3, d:4}]
#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE

@app.route("/api/v1.0/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league"
    )

#################################################
# Flask Routes
#################################################

# @TODO: Complete the routes for your app here
# YOUR CODE GOES HERE

if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE



if __name__ == "__main__":
    app.run(debug=True)