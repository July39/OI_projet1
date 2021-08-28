

import pymongo
from datetime import date
from datetime import datetime
from project1.constants import *


__all__ = ["get_events", "log_event"]


def get_events():

    client = pymongo.MongoClient(MONGODB_URI)
    db = client.project1
    col = db.events
    return col


def log_event(state: str):

    events = get_events()
    event = {
                "date":  date.today().strftime(DATE_FORMAT),
                "time":  datetime.now().strftime(TIME_FORMAT),
                "state": state
             }
    print(events.insert_one(event).inserted_id)

