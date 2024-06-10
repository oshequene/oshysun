import telebot
import requests

token = "7091051319:AAH4QbiU9TzIzEOJdscJNyS48PxY_-3mNko"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """اهلا في بوت يرسل رسائل الي رقم حساب تليكرام عن طريق رقم الهاتف 📱 ! ارسل الان رقمك مع رمز الدوله بهذه الشكل 👇🏻 .
مثال : 96411111111111+""")

@bot.message_handler(func=lambda message: True)
def verify_phone_number(message):
    try:
        phone = message.text
        headers = {
            'bot_id': '1288099309',
            'origin': 'https://t.me',
            'lang': 'en'
        }
        data = {
            'phone': f'{phone}'
        }
        response = requests.post('https://oauth.tg.dev/auth/request?bot_id=1288099309&origin=https://t.me&lang=en', headers=headers,data=data)
        bot.reply_to(message, 'تم ارسال الكود الى هذه رقم الهاتف 📨 !')
    except Exception as e:
        bot.reply_to(message, 'غير الرقم او ارسلة من جديد او الرقم غلط 📨 !')

bot.polling(none_stop=True)
