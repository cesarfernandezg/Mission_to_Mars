# use flask to render a template, redirectering to another url
from flask import Flask, render_template, redirect, url_for
# use PyMongo to interact wit our Mongo database
from flask_pymongo import PyMongo
import scraping

# set up flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set Up App Routes
# define the rout for the HTML
@app.route("/") # home page
def index():
   mars = mongo.db.mars.find_one() 
   return render_template("index.html", mars=mars)

# set up the scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars # mongo database
   mars_data = scraping.scrape_all() # hold the newly scraped data
   mars.update({}, mars_data, upsert=True) #update database
   return redirect('/', code=302) # navi our page back

if __name__ == "__main__":
   app.run()