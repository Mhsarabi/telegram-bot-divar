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


    

bot.infinity_polling()