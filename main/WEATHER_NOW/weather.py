import requests
import time

API = input("BOT: ENTER YOUR OPEN-WEATHER-API TOKEN :--- \t")
print("\n")

# API-ACCESS FUNCTION
def weather_data(query):

    try:
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID='+API+'&units=metric')
        print("LOADING...")
        time.sleep(2)
        return res.json();
    
    except:
        print("\nBOT: CAN'T ACCESS WEATHER API RIGHT NOW! PLEASE CHECK YOUR API-ID AND INTERNET CONNECTION!")
        exit();
        

# DISPLAY FUNCTION
def print_weather(result,city):
    
    print("----------------------------------**")
    print("{}'s temperature: {}°C ".format(city.upper(),result['main']['temp']))
    print("Feels like: {}°C ".format(result['main']['feels_like']))
    print("Minimum Temperature: {}°C ".format(result['main']['temp_min']))
    print("Maximum Temperature: {}°C ".format(result['main']['temp_max']))
    print("Pressure: {} Pascal ".format(result['main']['pressure']))
    print("Humidity: {} ".format(result['main']['humidity']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    print("Coordinates -- Longitude: {}° ".format(result['coord']['lon']))
    print("Coordinates -- Latitude: {}° ".format(result['coord']['lat']))
    print("Country Code: {} ".format(result['sys']['country']))
    print("----------------------------------**");


# DRIVER FUNCTION
def main():
    
    city=input('\nBOT: ENTER THE NAME OF THE PLACE [CITY] :---- \t')
    
    try:
        query='q='+city
        w_data=weather_data(query)
        print_weather(w_data, city)
    
    except:
        print('BOT: ERROR! THE CITY WAS NOT FOUND...! \n');


# DRIVER CODE..
main()
while (1):
    
    print("\n-----***----------***----------***----------***----------***-----")
    U = input("BOT: WANT TO CHECK FOR OTHER PLACES ?? ENTER [YES/Y  or  NO/N]:\t").lower()
    print("-----***----------***----------***----------***----------***-----\n")
    
    if U == "yes" or U == "y":
        main()
    
    elif U == "no" or U == "n":
        print("\nBOT: THANK YOU!")
        break
    
    else:
        print("\nWRONG INPUT!!")
        
        
        
@ CODED BY TSG405, 2021        
