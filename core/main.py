import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
import logging

# set logger
logger=telebot.logger
telebot.logger.setLevel(logging.INFO)

# set API Token and bot
API_TOKEN=os.environ.get("API_TOKEN")
bot=telebot.TeleBot(API_TOKEN)

# command start
@bot.message_handler(commands=['start'])
def start_command(message):
    markup=InlineKeyboardMarkup()
    button_about_us=InlineKeyboardButton("درباره ما",callback_data="about_us")
    button_get_avg=InlineKeyboardButton("گرفتن حدود قیمت کالا",callback_data="avg")
    button_get_10_product=InlineKeyboardButton("نمونه کالا",callback_data="product")
    button_guide=InlineKeyboardButton("راهنما",callback_data="guide")

    
    markup.add(button_about_us,button_get_avg,button_get_10_product,button_guide)

    bot.reply_to(message,text=f"""سلام {message.from_user.username} عزیز\n به ربات دیوار خیلی خوش آمدی🔥
                 \nوظیفه من این هست که سرویس هایی از سایت دیوار را به شما ارائه دهم
                 \nحالا به من بگو چه کمکی از دستم ساخته است🙏"""
                 ,reply_markup=markup)
    

bot.infinity_polling()