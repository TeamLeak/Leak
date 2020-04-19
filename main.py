import os
from api import API_addUser, API_checkUser, API_searchMarketCheck, API_carPreferences, API_carLikes
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack, send_from_directory
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)

# Setup Mongo
# app.config["MONGO_URI"] = os.environ['MONGODB_URI'] + "?retryWrites=false"
app.config["MONGO_URI"] = "mongodb://localhost:27017/bumper"
mongo = PyMongo(app)
users = mongo.db.users
car_preferences = mongo.db.car_preferences


api = Api(app)
api.add_resource(API_addUser, '/adduser')
api.add_resource(API_checkUser, '/checkuser')
api.add_resource(API_searchMarketCheck, '/search')
api.add_resource(API_carPreferences, '/car_preferences')
api.add_resource(API_carLikes, '/car_likes')


# Routing
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                              'bumper.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def init():
    return render_template('welcome/welcome.html')

@app.route('/welcome') 
def welcome():
    return render_template('welcome/welcome.html')

@app.route('/logout') 
def logout():
    return render_template('logout/logout.html')

@app.route('/search_page')
def search_page():
    return render_template('search/search_page.html')


@app.route('/likes')
def liked_cars():
    return render_template('likes/likes.html')


@app.route('/home', methods=['GET', 'POST'])
def home_screen():
    # if there's no id token or access token just show cardstarck and only only dislike of cars
    # Anything requring a specific user, states
    make = ""
    model = ""
    zip_code = ""
    radius = ""
    if request.method == 'POST':
        if request.form['make'] != None:
            make = request.form['make']
            model = request.form['model']
            zip_code = request.form['zip']
            radius = request.form['radius']
            # price_range = request.form['minPrice'] + "-" + request.form['maxPrice']
            if model == 'AllModels':
                model = ''

    return render_template('home/home.html', make=make, model=model, zip_code=zip_code, radius=radius)
