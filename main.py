def find_open_restaurants(csv_filename, search_datetime):
    with open (csv_filename) as file:
        readfile = file.read()
    print(readfile)


find_open_restaurants('restaurants.csv', 0)