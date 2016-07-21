from apiclient.discovery import build
from bs4 import BeautifulSoup
from . import app


GOOGLE_DEVELOPER_KEY = app.config['GOOGLE_DEVELOPER_KEY']
GOOGLE_BLOGGER_ID    = app.config['GOOGLE_BLOGGER_ID']
try:
    service = build('blogger','v3',developerKey=GOOGLE_DEVELOPER_KEY)
    posts = service.posts()
except:
    posts = []

def get_post_list():
    try:
        result = posts.list(blogId=GOOGLE_BLOGGER_ID, maxResults=3, fetchBodies=None,fetchImages=True).execute()
    except:
        result = []
    return result

def print_post_list():
    posts = get_post_list()
    print(posts)


if __name__ == "__main__":
    print_post_list()
