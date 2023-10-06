import phonenumbers
# from Phone_tracker import phone
from phonenumbers import geocoder

number = input("Enter your Ph. No. with +91: ")
phone_no = phonenumbers.parse(number)

location = geocoder.description_for_number(phone_no, "en")
print(location)

"""
# now we need GPS Tracker for tracing the phone in google map.:-
# for that we will install "opencage" package in terminal:-         pip install opencage
"""

# now, import "opencage" module.

import opencage
from opencage.geocoder import OpenCageGeocode

"""
# after importing opencage module will open "https://opencagedata.com/" webpage in our browser.
# after that we need to sing up our account..
# from there we get the API key ion demo..
"""

API_key = "311d83eefe1d426c84c0df4693ec8209"
geocoder = OpenCageGeocode(API_key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
'''
so, after running the code: "print(results)" we will get the latitude and longitude in our console.
# latitude as "lat" and longitude as "lng". from there we can find location. 
# but before that we will comment out "print(results)"
'''

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

# so, after running program we get our lat, & lng in console...

"""
# again we are installing "folium" package in terminal. #         pip install folium
# and import folium package.
"""
import folium

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(my_map)

# after lat, lng we created my_map variable to show location in the map.
# and also we should save our location.
# and this location file will be saved in ".html" format. so will save file in html format.

my_map.save("My_Location.html")















