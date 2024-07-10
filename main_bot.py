import telebot
from telebot import types
from my_bot_key import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Дуккинские озера")
    item2 = types.KeyboardButton("Софийские водопады")
    item3 = types.KeyboardButton("Софийские озера")
    item4 = types.KeyboardButton("Семицветное озеро")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}. Здесь Вы найдете треккинговые маршруты Архыза!")
    bot.send_message(message.chat.id, 'Выберите ниже, что Вам интересно)', reply_markup=markup)
    

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Дуккинские озера":
        bot.send_message(message.chat.id,f"{message.from_user.first_name}, ловите ссылку на информацию о данном маршруте) https://www.kp.ru/russia/arhyz/mesta/dukkinskie-ozera/")
        bot.send_message(message.chat.id, "И конечно, ловите вид сверху на озера))) https://ic.pics.livejournal.com/lev_zi/85369690/477455/477455_original.jpg ")
        bot.send_message(message.chat.id, "Можете написать в чат Хочу совет или Хочу пожелание!")
    elif message.text == "Софийские водопады":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, ловите ссылку на информацию о данном маршруте) https://www.kp.ru/russia/arhyz/mesta/sofijskie-vodopady/")
        bot.send_message(message.chat.id, "И конечно, ловите красивую фоточку на водопады))) https://a.d-cd.net/9MCHXwImtRBoV7RQHNqIyzJ76C4-1920.jpg")
        bot.send_message(message.chat.id, "Можете написать в чат Хочу совет или Хочу пожелание!")
    elif message.text == "Софийские озера":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, ловите ссылку на информацию о данном маршруте) https://www.kp.ru/russia/arhyz/mesta/sofijskie-ozera/")
        bot.send_message(message.chat.id, "И конечно, ловите вид на эти великолепные озера))) https://vsegda-pomnim.com/uploads/posts/2022-03/1648742723_55-vsegda-pomnim-com-p-sofiiskie-ozera-v-arkhize-foto-58.jpg")
        bot.send_message(message.chat.id, "!!! Данный маршрут относится к категории СЛОЖНЫХ маршрутов, пожалуйста при планировании путешествия, ПОМНИТЕ ОБ ЭТОМ !!!")
        bot.send_message(message.chat.id, "Можете написать в чат Хочу совет или Хочу пожелание!")
    elif message.text == "Семицветное озеро":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, ловите ссылку на информацию о данном маршруте) https://www.kp.ru/russia/arhyz/mesta/ozero-semitsvetnoe/")
        bot.send_message(message.chat.id, "Ловите красивую фоточку озера))) https://adrenalin.bike/wp-content/uploads/2016/04/3mQ6UaJHDQY.jpg")
        bot.send_message(message.chat.id, "Можете написать в чат Хочу совет или Хочу пожелание!")
    elif message.text == "Хочу совет":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, перед выходом на маршрут необходимо быть максимально отдохнувшим! Трезво оценивай свои силы, возможности и физическую подготовку")
        bot.send_message(message.chat.id,"Необходимо иметь треккинговую обувь и треккинговые палки! По ссылке ловите список на полный перечень Вашего рюкзака для комфортного путешествия!) https://dzen.ru/a/ZUJHO3Bqol6WK0GP ")
        bot.send_message(message.chat.id, "При первых походах лучше брать машину для докидки до маршрута. Средняя цена машины составляет от 5-8 т.р. Вариантов много в поселке, без проблем можно выбрать и очаровательной улыбкой или харизмой сбить цену))) ")
    elif message.text == "Хочу пожелание":
        photo = (open('345.jpg', 'rb'))
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, отличных Вам походов, головокружительных впечатлений и хорошей погоды (поверьте, в горах это очень важно!) !!!")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, выберите одну из кнопок ниже или напиши Хочу совет / Хочу пожелание")
bot.infinity_polling()