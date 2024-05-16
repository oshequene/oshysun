import os
try :
    import requests,telebot
    from telebot import *
    import random
    from time import *
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI==3.7.6')

bot = telebot.TeleBot("6972476993:AAFFusJfPIiPmXUtN0KDypcAaEmYHXLsUNg")

@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    name = message.from_user.first_name
    use = message.from_user.username
    key = types.InlineKeyboardMarkup()
    cam = types.InlineKeyboardButton('المــطور',url ='https://t.me/exxxix')
    bot14 = types.InlineKeyboardButton(f'''
  اضاف قناتك
''',callback_data='d1')
    photo = f"t.me/{message.from_user.username}"
    key.add(bot14)
    key.add(cam)
    bot.send_photo(message.chat.id,photo,f"""<strong>
مرحبًا {name} ، اهلاً بـك في بوت القرأن الكريم ☕🤍
• ارفع البوت ادمن في قناتك وافتح خاصية نشر الرسائل •
• قم بأرسال ID الخاص بقناتك مسبوقًا بــِ (100-) •
اذا كنت تجهل استخراج ايدي قناتك تواصل مع المطور 
</strong>""",parse_mode="html",reply_to_message_id=message.message_id,reply_markup=key,timeout=3.5)	
    


    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "d1":
        	d1(message,call)
             



def d1(message,call):
    bot.send_message(message.chat.id, text=f"""<strong>• ارفع البوت ادمن في قناتك وافتح خاصية نشر الرسائل •
• قم بأرسال ID الخاص بقناتك مسبوقًا بــِ (100-) •
اذا كنت تجهل استخراج ايدي قناتك تواصل مع المطور 
@exxxix </strong>""",parse_mode="html",timeout=3.5)
@bot.message_handler(func=lambda message: True)
def start(message):
        us = message.text
        bot.send_message(message.chat.id, text=f"<strong>تم اضافة القناة إلى الإرسال التلقائي . سيتم ارسال اية قرانية عشوائيه كل 24 ساعة إلى القناة ✅</strong>",parse_mode="html",timeout=1)
        while True : 
            random_ayah_number = random.randint(1, 6236)
            api_url = f"https://api.alquran.cloud/v1/ayah/{random_ayah_number}/image"
            response = requests.get(api_url)
            if response.status_code == 200:
                req = response.json()['data']
                aih = req['text']
                surah = req['surah']['number']
                surah_name = req['surah']['name']
                key = types.InlineKeyboardMarkup()
                bot14 = types.InlineKeyboardButton('البــوت',url ='https://t.me/oshysitebot')
                key.add(bot14)

                bot.send_message(us,text=f"""<strong> قال تعالى : ({aih}) </strong>""",parse_mode="html",reply_markup=key,timeout=1)
                sleep(82000)





bot.infinity_polling()
