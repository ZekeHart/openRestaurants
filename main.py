import csv
from datetime import datetime, time, date
import re


dt_now = datetime.now()

def find_open_restaurants(csv_filename, search_datetime):
    search_weekday = search_datetime.strftime("%a")
    search_time = search_datetime.time()
    restaurant_info_dict = {}
    with open (csv_filename) as file:
        readfile = csv.DictReader(file)
        for line in readfile:
            restaurant_info_dict[line['Restaurant Name']] = line['Hours']
    open_on_day = checkDay(search_weekday, restaurant_info_dict)
    print(open_on_day)
    # open_restaurants = checkTime(search_time)
            
    
        # if 'Mon' in restaurant_info_dict[pair]:

def checkDay(day, restaurant_dict):
    open_on_day = {}
    for restaurant in restaurant_dict:
        if day in restaurant_dict[restaurant]:
            open_on_day[restaurant] = restaurant_dict[restaurant]
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