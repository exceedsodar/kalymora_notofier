import json
import datetime

def get_data():
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary

    data = json.load(f)
    # Closing file
    f.close()
    return data

def is_weekend():
    weekno = datetime.datetime.today().weekday()
    if weekno < 5:
        return False
    else:  # 5 Sat, 6 Sun
        return  True
