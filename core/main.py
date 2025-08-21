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

# Response buttons
@bot.callback_query_handler(func= lambda call:True)
def response_buttons(call):
    if call.data=="about_us":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,
                              text="""خب دوست من همونطور که قبلا اشاره کرده بودم من ربات دیوار هستیم
                              \nوظیفه من این است که برای اینکه شما راحت باشی و لازم نباشه بری تو گوگل و دیوار را سرچ کنی و...
                              \nآقا جان من اینجام😅
                              \nغصه چی را می خوری؟😁
                              \nفقط لب ترک کن و دیتایی که از دیوار می خوای را به من بگو تا بهت تحویل بدم🔥
                              \nکسی که من را ساخته اسمش محسن سرابی هستش البته بگم هااا زیاد باهاش حال نمی کنم😒
                              \nولی خب با این حال اگر خواستی به پورتفولیو آن یک سر بزن، بچه بدی نیست😜
                              \nhttps://www.mhsrbi.ir/
                              """)

    if call.data=="guide":
       bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,
                              text="""خب ظاهرا به یکم راهنمایی نیاز داری برای کار کردن با من🧐
                              \n/price:اگر این کامند را بزنی یعنی یک حدود قیمتی می خوای برای محصولی که الان تو ذهنت هست و خب من هم بعد از اینکه محصول وشهر مدنظرت را گفتی اون رنج قیمتش را بهت میگم
                              \n/product:با زدن این کامند و در ادامه با دادن شهر و محصول مدنظر چند تا محصولی از آن چیزی که انتخاب کردی را برات می فرستم
                              \n/about:با زدن این کامند اطلاعاتی در خصوص من و توسعه دنده من دریافت می کنی🙈
                              \n/guide:اینم از کامند راهنما هستش،می خوای اینو بزنییی؟خب من که الان راهنماییت کردم😐
                              """) 
    
    if call.data=="product":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="""خب پس چرا معطلی؟!😭
                              \nقصد خرید چه محصولی را داری؟
                              \nاسم آن را برام بنویس
                              """)
    
    if call.data=="avg":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="""راجب چه محصولی می خوای رنج قیمتیش را بدونی؟🤓
                              \nآن محصول را برام بنویس
                              """)


bot.infinity_polling()