

import pymongo
from datetime import date
from datetime import datetime
from project1.constants import *


__all__ = ["get_events", "log_event"]


events = None


def get_events():

    global events

    if events is None:
        client = pymongo.MongoClient(MONGODB_URI)
        db = client.project1
        events = db.events

    return events

def log_event(msg):

    events = get_events()
    event = {
                "date":  date.today().strftime(DATE_FORMAT),
                "time":  datetime.now().strftime(TIME_FORMAT),
                "id": msg['id'],
                "cmd": msg['cmd'],
             }
    print(events.insert_one(event).inserted_id)

