from . import app
from flask import render_template, url_for, request, g
from os import listdir
from . import blogger
from werkzeug.contrib.cache import SimpleCache
import db
from dateutil.parser import parse
import datetime

image_folder_thumbnails = app.static_folder + "/images/PreviewImages/thumbnails"
image_folder_large      = app.static_folder + "/images/PreviewImages/fullsize"
image_folder_recipes    = app.static_folder + "/images/recipes"

cache = SimpleCache()


@app.url_defaults
def add_blog_posts(endpoint,values):
    cache_key = 'blog-posts'
    blog_posts = cache.get( cache_key )
    if blog_posts is None:
        blog_posts = blogger.get_post_list()
        cache.set( cache_key,blog_posts,timeout=5*60 )

    g.posts = blog_posts
    g.js_file = app.config['JSMAIN']


@app.route('/')
def index():

    thumbnails = get_images_from_dir(image_folder_thumbnails)
    fullsize   = get_images_from_dir(image_folder_large)
    stores     = get_list_of_stores()
#     events     = get_list_of_events()
    return render_template('index.html', thumbnails=thumbnails, fullsize=fullsize, stores=stores, events=events)

@app.route('/press/')
def press():
    return render_template('press.html', events=events)

@app.route('/author/')
def author():
    return render_template('author.html', events=events)

@app.route('/privacy/')
def privacy():
    return render_template('privacy.html', events=events)


@app.route('/recipes/')
def recipes():
    recipe_images = get_images_from_dir(image_folder_recipes)
    return render_template('recipes.html', recipe_images = recipe_images, events=events)



def get_images_from_dir(image_folder):
    return listdir(image_folder)


def get_list_of_stores():

    try:
        stores = db.stores
        store_list = stores.find().sort("county")
    except Exception:
        store_list = []

    return store_list

def get_list_of_events():
    try:
        events = db.events
        events_list = events.find({'parsed_date':{"$gt":datetime.datetime.today()}}).sort("parsed_date")
    except Exception:
        events_list = []

    return events_list

events     = get_list_of_events()


@app.template_filter('format_date')
def _jinja_filter_datetime(date, fmt=None):
    date = parse(date)
    native = date.replace(tzinfo=None)
    format='%a %b %d, %Y'
    return native.strftime(format)
