import csv
from datetime import datetime, time
import time

dt_now = datetime.now()

def find_open_restaurants(csv_filename, search_datetime):
    search_weekday_int = search_datetime.weekday()
    search_time = search_datetime.time()

    
    restaurant_info_dict = {}
    with open (csv_filename) as file:
        readfile = csv.DictReader(file)
        for line in readfile:
            restaurant_info_dict[line['Restaurant Name']] = line['Hours']
            
    # for pair in restaurant_info_dict:
    print(search_time)
    print(search_weekday_int)
    # print(restaurant_info_dict['Yard House'])
    # for line in readfile:
    #     restaurant_info_dict


find_open_restaurants('restaurants.csv', dt_now)