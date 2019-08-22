import csv
from datetime import datetime, time, date
import re


def find_open_restaurants(csv_filename, search_datetime):
    """
    Given a csv with Restaurant Name and Hours as the two categories and a datetime object,
    reads in the info from the csv into a dictionary, then calls functions to see which
    restaurants are open on that day and time
    """
    search_weekday = search_datetime.strftime("%a")
    search_time = search_datetime.time()
    restaurant_info_dict = {}
    with open (csv_filename) as file:
        readfile = csv.DictReader(file)
        for line in readfile:
            restaurant_info_dict[line['Restaurant Name']] = line['Hours']
    open_on_day = checkDay(search_weekday, restaurant_info_dict)
    open_restaurants = checkTime(search_time, open_on_day)
    print(open_restaurants)
            

def checkDay(day, restaurant_dict):
    """
    given a day and a dictionary of restaurant names and their hours in a specific format,
    e.g., "Mon-Fri 10:30 am - 9:30 pm  / Sat-Sun 10 am - 9:30 pm"
    returns a dict with the restaurant names that are open on that day 
    and the relevant chunk of hours that correspond to that day
    """
    open_on_day = {}
    for restaurant in restaurant_dict:
        if "Mon-Sun" in restaurant_dict[restaurant]:
            open_on_day[restaurant] = restaurant_dict[restaurant]
        else:
            if '/' in restaurant_dict[restaurant]:
                split_hours = restaurant_dict[restaurant].split('/')
            else:
                split_hours = restaurant_dict[restaurant]
            for chunk in split_hours:
                if day in chunk:
                    open_on_day[restaurant] = chunk
                elif day == 'Tue':
                    if 'Mon-' in chunk:
                        open_on_day[restaurant] = chunk
                elif day == 'Wed':
                    if ('Tue-' in chunk) or ('-Thu' in chunk) or ('Mon-Fri' in chunk) or ('Mon-Sat' in chunk):
                        open_on_day[restaurant] = chunk
                elif day == 'Thu':
                    if ('Wed-' in chunk) or ('-Fri' in chunk) or ('Mon-Sat' in chunk) or ('Tue-Sat' in chunk) or ('Tue-Sun' in chunk):
                        open_on_day[restaurant] = chunk
                elif day == 'Fri':
                    if ('Thu-' in chunk) or ('-Sat' in chunk) or ('Tue-Sun' in chunk) or ('Wed-Sun' in chunk):
                        open_on_day[restaurant] = chunk
                elif day =="Sat":
                    if ('-Sun' in chunk):
                        open_on_day[restaurant] = chunk
    return open_on_day


def checkTime(time_of_day, restaurant_info_dict):
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
        time_dict['start time'] = re.sub(' ', '',time_string.split('-')[0])
        time_dict['end time'] = re.sub(' ', '', time_string.split('-')[1])
        if ':' in  time_dict['start time']:
            time_dict['start time'] = datetime.strptime(time_dict['start time'], '%I:%M%p')
        else:
            time_dict['start time'] = datetime.strptime(time_dict['start time'], '%I%p')
        if ':' in  time_dict['end time']:
            time_dict['end time'] = datetime.strptime(time_dict['end time'], '%I:%M%p')
        else:
            time_dict['end time'] = datetime.strptime(time_dict['end time'], '%I%p')
        
        if time_of_day >= time_dict['start time'].time() and time_of_day >= time_dict['start time'].time():
            open_restaurants.append(restaurant)
    return open_restaurants


if __name__ == "__main__":
    dt_now = datetime.now()
    find_open_restaurants('restaurants.csv', dt_now)