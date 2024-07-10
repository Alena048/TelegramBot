import requests
import telebot
from key import API_key, API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def hello_message(message):
    bot.send_message(message.chat.id, f"Привет! {message.from_user.first_name} Для получения погоды, введите название города)")

@bot.message_handler(content_types="text")
def get_weather(message):
    city_name = message.text
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru'
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        bot.send_message(message.chat.id, f'Погода в городе: {city} \nТемпература: {cur_weather} \nВлажность: {humidity}\nСкорость ветра: {wind}м/с\nОблачность: {description}')
        # return (f'Погода в городе: {city} \nТемпература: {cur_weather} \nВлажность: {humidity}\nСкорость ветра: {wind}м/с\nОблачность: {description}')
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "Неверно указан город")

bot.infinity_polling()