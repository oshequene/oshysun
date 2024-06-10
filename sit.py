import telebot
from telebot.types import InlineKeyboardButton as btn , InlineKeyboardMarkup as Mar
'''
تذكر مصريي هااا
مبرمج ملف : @BRoK8
قناتي : @Crrazy_8
'''
token = "6972476993:AAFFusJfPIiPmXUtN0KDypcAaEmYHXLsUNg"
bot = telebot.TeleBot(token)
bot_info = bot.get_me()
btn = Mar().add(btn(text='• ضيفني لمجموعتك •',url=f"https://t.me/{bot_info.username}?startgroup=start"))

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message,'اهلاً انا بوت لتنظيم القروبات و القنوات .\nبعد كُل رسالة ارسل شرطة',reply_markup=btn)

@bot.message_handler(func=lambda message:True)
def ss(message):
	url = 'https://t.me/exixxx/69'
	bot.send_animation(message.chat.id,url)
	
bot.polling(True)
