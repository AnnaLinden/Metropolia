#task - make a dictionary with countries
#task - get time from api to the function def get_time()
#https://timeapi.io/

import random
airports = ["Amsterdam Airport Schiphol", "Berlin Brandenburg Airport", "Charles de Gaulle International Airport",
            "Copenhagen Kastrup Airport", "Dublin Airport", "Geneva Cointrin International Airport", "Gran Canaria Airport",
            "Helsinki Vantaa Airport", "Lennart Meri Tallinn Airport", "Lviv International Airport",
            "London Gatwick Airport",  "Luxembourg-Findel International Airport", "Milan Bergamo Airport",  "Oslo Airport",
            "Gardermoen", "Riga International Airport", "Sheremetyevo International Airport", "Vilnius International Airport",
            "Warsaw Chopin Airport", "Zagreb Airport"]

#select airport.name, country.name from airport, country where airport.iso_country = country.iso_country and
# airport.type = "large_airport" and country.continent = "EU";

def get_random_airport():
    airport = random.choice(airports)
    print("Number of items in the list = ", len(airports))
    return airport


    #to check the length of the airport list


def get_city_name():
    city = None
    return city

def get_time():
    time = None
    return time

name = (input("Enter your name: ")).title()
airport = get_random_airport()
city = get_city_name()
time = get_time()

print (f"Hello, {name}! You are in {airport} in {city}. ")
print(f"The time is {time}")