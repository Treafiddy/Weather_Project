import requests 
api_key = "e2712931bb11f9b4756a42fabd17c703"

print("Welcome to the weather app.")


def city_weather():
    try:  
        user_input = input("Enter a city: ")
        weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")
        weather = weather_data.json()['weather'][0]["main"]
        temp = weather_data.json()["main"]["temp"]
        print(f"The weather is {weather} and the temperature is {temp}°C")
    except KeyError:
        cities = ["London", "Paris", "Tokyo", "Dubai", "Bangkok", "Hong Kong", "Singapore", "Rome", "Istanbul", "Harrogate"]
        if len(user_input) >= 3:
            user_len = user_input[:3].lower()  # Convert to lowercase for case-insensitive comparison
            for city in cities:
                if len(city) > 3:
                    cities_len = city[:3].lower()
                    if user_len == cities_len:
                        print(f"We think you meant {city}.")
                        weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
                        weather = weather_data.json()['weather'][0]["main"]
                        temp = weather_data.json()["main"]["temp"]
                        print(f"The weather is {weather} and the temperature is {temp}°c.")

city_weather()





