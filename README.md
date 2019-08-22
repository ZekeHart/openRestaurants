# openRestaurants

This contains a function find_open_restaurants which takes a csv filename and a datetime object as parameters. It returns a list of the restaurants that are open at that time. It also contains two smaller functions that find_open_restaurants uses, check_day which takes a shortened weekday name and checks to see what restaurants are open on that day, and check_time which takes a datetime.time() object and a dictionary with restaurants and times and returns a list of restaurants that are open at that time.

## Instructions

If main.py is run directly then it runs using restaurants.csv and a datetime.now() object. Otherwise if find_open_restaurants is imported and run in a different file then it will let you test it with other files or datetimes.
