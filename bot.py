import os
from telebot import *
from telebot.types import (
InlineKeyboardMarkup as Mk ,InlineKeyboardButton as btn)
Token = ("6972476993:AAFFusJfPIiPmXUtN0KDypcAaEmYHXLsUNg") # Token the bot
smdo = (2053519887) # ID the owner
id_channel = (-1001778635562) # ID
bot = TeleBot(Token)
ch = bot.get_chat(id_channel)
link = Mk().add(btn(text=f'{ch.title}',url=f't.me/{ch.username}'))
@bot.message_handler(commands=['start'])
def start(msg):
	photo = f"t.me/{msg.from_user.username}"
	if msg.chat.type == 'private' :
		if msg.chat.id != smdo:
			link = Mk().add(btn(text=f'{ch.title}',url=f't.me/{ch.username}')) 
			bot.send_photo(msg.chat.id,photo,f'''
*•  اهلا بـك في بوت السايت🫦. 
- ارسل رسالتك وسيتم نشرها بالقناة بعد موافقة المالك 👇🏻 📢.*''',
			parse_mode='Markdown',reply_markup=link)
		else:bot.send_message(msg.chat.id,'خير حبيبي المالك؟')
@bot.message_handler(content_types=['text'])
def text(msg):
	photo = f"t.me/{msg.from_user.username}"
	global id
	if msg.chat.type == 'private':
		id = msg.chat.id 
		open(f'{id}.txt','w').write(msg.text)
		bot.send_photo(msg.chat.id,'تم توجيه رسالتك الى المالك في انتظار الموافقة🤝🏻🤍..')

		key = Mk()
		key.add(btn(text='• المرسل •',url=f'tg://user?id={id}'))
		key.add(btn(text='• قبول •',callback_data='ok'),
		btn(text='• رفض •',callback_data='no'))
		bot.send_message(smdo,f'- الرساله : {msg.text} .',reply_markup=key)
@bot.callback_query_handler(func=lambda message:True)
def types(call):
	if call.data == 'ok':
		join=Mk().add(btn(text='• انشـر رسالتـك •',url=f't.me/{bot.get_me().username}'))
		txt = open(f'{id}.txt','r').read()
		bot.send_message(ch.id,f'- الرساله : {txt} .',reply_markup=join)
		bot.send_message(id,'تم نشر رسالتك بالقناة 👇🏻.',reply_markup=link)
		os.remove(f'{id}.txt')
		bot.delete_message(smdo,call.message.message_id)
	if call.data == 'no':
		os.remove(f'{id}.txt')
		bot.delete_message(smdo,call.message.message_id)
		bot.send_message(id,'- رفضت رسالتك .\n- قُل خَيراً أو أصمت .!')
bot.infinity_polling()
