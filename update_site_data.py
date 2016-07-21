from utilities import events
from utilities import stores


update_list = "/Volumes/InternalStorage/Storage/Dropbox/Wineries of the Sierra Foothills/BOOK WEBSITE/site_data"
stores_list = update_list + "/where_books_are_sold.txt"
events_list = update_list + "/events.txt"

def update_stores_list():
    stores.update_database(stores_list)


def update_events_list():
    events.update_events_database(events_list)

def main():
    update_stores_list()
    update_events_list()

main()
