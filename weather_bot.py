import requests
from pprint import pprint
from key import API_TOKEN, API_key

def get_weather(city, API_key):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=ru'
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print(f'Погода в городе: {city} \nТемпература: {cur_weather} \nВлажность: {humidity}\nСкорость ветра: {wind}м/с\nОблачность: {description}')
    except Exception as ex:
        print(ex)
        print("Произошла ошибка")

def main():
    city = input("Введите город: ")
    get_weather(city, API_key)

if __name__ == '__main__':
    main()