import requests
import telebot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak
from telebot import types
token = "7068446707:AAGE4lonyQtOKPkL910MAwBAau3ytN9Nw5k"
bot = telebot.TeleBot(token)
# @Crrazy_8 & @BRoK8
sent_video_messages = {}

@bot.message_handler(commands=["start"])
def start(message):
    L7N1 = types.InlineKeyboardMarkup()
    L7Nbut1 = types.InlineKeyboardButton("start",callback_data="L7Nbut1")    
    L7N1.add(L7Nbut1)
    photo = f"t.me/{message.from_user.username}"
    L7Ncall = f"[{message.from_user.first_name}]({photo})"
    text = f"""*-Hello* {L7Ncall} *in Bot Download videos from Instagram*"""
    bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7N1)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
        	   if call.data == "L7Nbut1":
        	   	messag=bot.send_message(chat_id=call.message.chat.id,text ="""
* | البوت مختص بتحميل الفديوات من انستقرام مثل ريلز او IGTV
| فقط ارسل رابط الفديو وانتظر 60 ثانية |
dev : @exxxix | @exixxx *
""",parse_mode='Markdown')
@bot.message_handler(content_types=['text'])
def Down(message):
    try:
    	link = message.text
    	json_data = {
    	    'url': link
    	}
    	response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()
    	thu = response['post_video_thumbnail']
    	video = response['post_video_url']
    	
    	sent_message = bot.send_photo(message.chat.id, thu, reply_to_message_id=message.message_id, reply_markup=Mak().add(Btn('تحميل الفيديو', callback_data='vid')))
    	
    	sent_video_messages[sent_message.message_id] = video
    except:
    	bot.reply_to(message,'Invalid link')

@bot.callback_query_handler(func=lambda call: call.data == 'vid')
def all(call):
    message_id = call.message.message_id
    if message_id in sent_video_messages:
        video = sent_video_messages[message_id]
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Mn = f"[المــطور](exxxix.t.me)"
        bot.send_video(call.message.chat.id,video,caption=Mn,parse_mode="Markdown")
        
bot.infinity_polling()
