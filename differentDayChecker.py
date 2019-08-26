import csv
from datetime import datetime
import re


def find_open_restaurants(csv_filename, search_datetime):
    """
    Given a csv with Restaurant Name and Hours as the two categories and a datetime object,
    reads in the info from the csv into a dictionary, then calls functions to see which
    restaurants are open on that day and time
    """
    search_weekday = search_datetime.weekday()
    search_time = search_datetime.time()
    restaurant_info_dict = {}
    with open (csv_filename) as file:
        readfile = csv.DictReader(file)
        for line in readfile:
            restaurant_info_dict[line['Restaurant Name']] = re.sub(' |day', '', line['Hours'])
    open_on_day = check_day(search_weekday, restaurant_info_dict)
    # open_restaurants = check_time(search_time, open_on_day)
    # print(open_restaurants)
            

def check_day(day, restaurant_dict):
    """
    given a day and a dictionary of restaurant names and their hours in a specific format,
    e.g., "Mon-Fri 10:30 am - 9:30 pm  / Sat-Sun 10 am - 9:30 pm"
    returns a dict with the restaurant names that are open on that day 
    and the relevant chunk of hours that correspond to that day
    """
    open_on_day = {}
    for restaurant in restaurant_dict:
        if '/' in restaurant_dict[restaurant]:
            split_hours = restaurant_dict[restaurant].split('/')
            for chunk in split_hours:
                first_time_index = re.search('\d', chunk)
                time_string = chunk[first_time_index.start():]
                day_string = chunk[:first_time_index.start()]
                to_check = replaceWeekdays(day_string)
        else:
            split_hours = restaurant_dict[restaurant]
            first_time_index = re.search('\d', split_hours)
            time_string = split_hours[first_time_index.start():]
            day_string = split_hours[:first_time_index.start()]
            to_check = replaceWeekdays(day_string)
        
        print(restaurant)
        print(time_string)
        print(day_string)

            #     elif day == 'Tue':
            #         if ('Mon-' in chunk) or ('-Wed' in chunk) or ('Sun-Thu' in chunk) or ('Sun-Fri' in chunk):
            #             open_on_day[restaurant] = chunk
            #     elif day == 'Wed':
            #         if ('Tue-' in chunk) or ('-Thu' in chunk) or ('Mon-Fri' in chunk) or ('Mon-Sat' in chunk):
            #             open_on_day[restaurant] = chunk
            #     elif day == 'Thu':
            #         if ('Wed-' in chunk) or ('-Fri' in chunk) or ('Mon-Sat' in chunk) or ('Tue-Sat' in chunk) or ('Tue-Sun' in chunk):
            #             open_on_day[restaurant] = chunk
            #     elif day == 'Fri':
            #         if ('Thu-' in chunk) or ('-Sat' in chunk) or ('Tue-Sun' in chunk) or ('Wed-Sun' in chunk):
            #             open_on_day[restaurant] = chunk
            #     elif day =="Sat":
            #         if ('-Sun' in chunk):
            #             open_on_day[restaurant] = chunk
    return open_on_day


def check_time(time_of_day, restaurant_info_dict):
    """
    Given a dictionary of restaurants and their hours, and a datetime time object, 
    goes through the restaurants and generates dictionaries with datetime objects
    for the start and close times, then sees if the datetime time objects falls
    between those times
    """
    open_restaurants = []
    for restaurant in restaurant_info_dict:
        first_time_index = re.search('\d', restaurant_info_dict[restaurant])
        time_string = restaurant_info_dict[restaurant][first_time_index.start():]
        time_dict = {}
        # removing spaces when adding to dictionary because there were some irregular spaces in end times,
        # figured I might as well do the same for start even though those were predictable in case future
        # cases are not
        time_dict['start time'] = time_string.split('-')[0]
        time_dict['end time'] = time_string.split('-')[1]
        if ':' in  time_dict['start time']:
            time_dict['start time'] = datetime.strptime(time_dict['start time'], '%I:%M%p')
        else:
            time_dict['start time'] = datetime.strptime(time_dict['start time'], '%I%p')
        if ':' in  time_dict['end time']:
            time_dict['end time'] = datetime.strptime(time_dict['end time'], '%I:%M%p')
        else:
            time_dict['end time'] = datetime.strptime(time_dict['end time'], '%I%p')
        
        if (time_of_day >= time_dict['start time'].time()) and (time_of_day <= time_dict['end time'].time()):
            open_restaurants.append(restaurant)
    return open_restaurants

def replaceWeekdays(day_string):
    replaceDict = {
        "Sun":0,
        "Mon":1,
        "Tue":2,
        "Wed":3,
        "Thu":4,
        "Fri":5,
    }

if __name__ == "__main__":
    dt_now = datetime.now()
    find_open_restaurants('restaurants.csv', dt_now)