import telebot
import requests
import json


bot = telebot.TeleBot('8402633139:AAFvGWEPAaNPxg36ZnfNn7mLdb-K0EAr884')
API = '57c4288add8cba15238bddcf1159ec7a'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>hi! i am wither bot</b> \n<i>Enter your city so I can give you an accurate weather forecast.</i>',parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def get_wither(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        icon = data['weather'][0]['icon']
        image_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

        bot.send_photo(message.chat.id, image_url, parse_mode="HTML")
        bot.send_message(
            message.chat.id,
            f"🌦️ <b><i>Current weather:</i></b> {data['weather'][0]['description'].capitalize()}\n\n"
            f"🌡️ <b>Max temperature:</b> {data['main']['temp_max']}°C\n"
            f"❄️ <b>Min temperature:</b> {data['main']['temp_min']}°C\n"
            f"💨 <b>Pressure:</b> {data['main']['pressure']} hPa\n"
            f"💧 <b>Humidity:</b> {data['main']['humidity']}%\n",
            parse_mode="HTML"
        )
    else:
        bot.reply_to(message, 'You were leading a non-existent city')
bot.polling(none_stop= True)




# {'coord': {'lon': -0.1257, 'lat': 51.5085},
# 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
# 'base': 'stations',
# 'main': {'temp': 15.2, 'feels_like': 14.55, 'temp_min': 14.41, 'temp_max': 16.66, 'pressure': 996, 'humidity': 68, 'sea_level': 996, 'grnd_level': 992},
# 'visibility': 10000,
# 'wind': {'speed': 2.06, 'deg': 220},
# 'clouds': {'all': 40},
# 'dt': 1761141539,
# 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1761114984, 'sunset': 1761151993},
# 'timezone': 3600,
# 'id': 2643743,
# 'name': 'London',
# 'cod': 200}