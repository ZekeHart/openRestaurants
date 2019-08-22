import csv
from datetime import datetime, time, date
import re


dt_now = datetime.now()

def find_open_restaurants(csv_filename, search_datetime):
    search_weekday = search_datetime.strftime("%a")
    print(search_weekday, type(search_weekday))
    search_time = search_datetime.time()
    restaurant_info_dict = {}
    with open (csv_filename) as file:
        readfile = csv.DictReader(file)
        for line in readfile:
            restaurant_info_dict[line['Restaurant Name']] = line['Hours']
    open_on_day = checkDay(search_weekday, restaurant_info_dict)
    print(open_on_day)
    # open_restaurants = checkTime(search_time, open_on_day)
            

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

    for pair in restaurant_info_dict:

        first_time_index = re.search("\d", restaurant_info_dict[pair])
        if restaurant_info_dict[pair][first_time_index.start()+1] not in ['0','1','2']:
            first_end_index = first_time_index.start() + 1
        else:
            first_end_index = first_time_index.start() + 2
        firstStartTime = datetime.strptime(restaurant_info_dict[pair][first_time_index.start() : first_end_index], "%I")
        print(firstStartTime)

#     print(search_time)
#     print(search_weekday_int)
#     print(restaurant_info_dict['Yard House'].split()[1:3])
#     restaurant_info_dict['Yard House'].split()
#     print(restaurant_info_dict['Yard House'])

find_open_restaurants('restaurants.csv', dt_now)