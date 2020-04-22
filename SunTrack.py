import urllib.parse     # Needs to ne pip installed and imported before running. 
import requests         #
import time             #
import datetime         #
import pytz             #  
import tzlocal          #


main_api = "https://api.sunrise-sunset.org/json?"  # These are the url's this program uses to get information.
location_api = "http://www.mapquestapi.com/geocoding/v1/address?" #
key = "Your own API key" # You need to input your own API key, which you can get by making developer account on mapquestapi.com.

while True: # I have made this program inside while-loop.
    loc = input("Name the city that you want to see sunrise and sunset times (or quit by ""q""): ") # First user inputs city, they want to see sunrise and sunset times.
    if loc == "q" or loc == "quit": # If input is 'q' or 'quit', program exits.
        break
    
    url2 = location_api + urllib.parse.urlencode({"key":key,"location":loc}) # Parses user inputs 'key' and 'loc' into the url.
    json_data2 = requests.get(url2).json() # Making request to the API.
    json_status2 = json_data2["info"]["statuscode"] # Checking the status code, if API is available.
    a = json_data2["results"][0]["locations"][0]["latLng"]["lat"] # Getting the latitude.
    b = json_data2["results"][0]["locations"][0]["latLng"]["lng"] # Getting the longitude of the city 
    
    print("==============================================") # I'm printing these, to make the output more clear for user.
    if json_status2 == 0: # If API is available, prints 'successful route call' + status code.
        print("API Status: " + str(json_status2) + " = A successful route call. \n") #
        
    url = main_api + urllib.parse.urlencode({"lat":a, "lng":b}) # Parses information got from the other api 'lat'(a) and 'lon'(b) into the url.
    json_data = requests.get(url).json() # Making request to the API.

    print("==============================================") # I'm printing these, to make the output more clear for user.
    print("URL: " + (url2)) # Prints the first url.
    print("URL: " + (url)) # Prints the second url.
    print("==============================================") # I'm printing these, to make the output more clear for user.
    
    json_status = json_data["status"] # Checking the status code, if API is available.
    c = json_data["results"]["sunrise"] # Getting the sunrise time.
    d = json_data["results"]["sunset"] # Getting the sunset time.
    r = tzlocal.get_localzone() # Taking user local timezone, from their computers timesettings.
    f = datetime.datetime.strptime(c, "%I:%M:%S %p") # Editing the sunrise time into the user local time.
    h = datetime.datetime.strptime(d, "%I:%M:%S %p") # Editing the sunset time into the user local time.
    g = (f.replace(tzinfo=pytz.utc).astimezone(r)) # Inputting edited sunrise time and change it to the local timezone.
    j = (h.replace(tzinfo=pytz.utc).astimezone(r)) # Inputting edited sunset time and change it to the local timezone.

    if json_status == "OK": # Checking if second API is available.
        print("API Status: " + str(json_status) + " = A successful route call. \n") # If API is available, prints 'successful route call' + status code.
        print("==============================================") # I'm printing these, to make the output more clear for user.
        print("Sun will rise at: " + datetime.datetime.strftime(g, "%H:%M:%S")) # Printing sunrise time using local timezone.
        print("Sun will set at: " + datetime.datetime.strftime(j, "%H:%M:%S")) # Printing sunset time using local timezone.
        print("==============================================") # I'm printing these, to make the output more clear for user.
    
    elif json_status != "OK": # If API is not available, give error code.
        print("\n****************************************************************") # I'm printing these, to make the output more clear for user.
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both coordinates.") # Usually error is caused by miss spelling, so program recommend to check spelling.
        print("****************************************************************\n") # I'm printing these, to make the output more clear for user.
