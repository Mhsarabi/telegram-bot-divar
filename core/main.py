import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
import logging
from request_divar import get_products,get_avg_price_from_divar

# set logger
logger=telebot.logger
telebot.logger.setLevel(logging.INFO)

# set API Token and bot
API_TOKEN=os.environ.get("API_TOKEN")
bot=telebot.TeleBot(API_TOKEN)

# add channel setting
CHANEL_ID=os.environ.get("CHANEL_ID")

# status of user(average or product)
user_status={}

# is joined to channel
is_joined=False

# join to channel
def is_member(message):
    user_info=bot.get_chat_member(CHANEL_ID,message.from_user.id)
    if not user_info.status in ["administrator","creator","member"]:
        bot.send_message(chat_id=message.chat.id,text="""ااااام دوست من شرمنده ام😅😬
                         \nولی قبل از اینکه دستورات شما را نجام بدم باید عضو کانال زیر شوید
                         \nمنم مثل خودت از حرف زور خوشم نمیاد😤
                         \nولی چاره ای نیست، خوشحال میشم بعد از اینکه عضو کانال زیر شدی با هم همکاری کنیم❤️
                         \n https://t.me/+9UeYvNDCL18yZThk""")
        is_joined=False
        return is_joined
    else:
        is_joined=True
        return is_joined

# command start
@bot.message_handler(commands=['start'])
def start_command(message):
    is_joined=is_member(message)
    if is_joined:
        markup=InlineKeyboardMarkup()
        button_about_us=InlineKeyboardButton("درباره ما",callback_data="about_us")
        button_get_avg=InlineKeyboardButton("گرفتن حدود قیمت کالا",callback_data="avg")
        button_get_10_product=InlineKeyboardButton("نمونه کالا",callback_data="product")
        button_guide=InlineKeyboardButton("راهنما",callback_data="guide")
        button_support=InlineKeyboardButton("پشتیبانی",callback_data="support")


        
        markup.add(button_about_us,button_get_avg,button_get_10_product,button_guide,button_support)

        bot.reply_to(message,text=f"""سلام {message.from_user.username} عزیز\n به ربات دیوار خیلی خوش آمدی🔥
                    \nوظیفه من این هست که سرویس هایی از سایت دیوار را به شما ارائه دهم
                    \nحالا به من بگو چه کمکی از دستم ساخته است🙏"""
                    ,reply_markup=markup)

# Response buttons
@bot.callback_query_handler(func= lambda call:True)
def response_buttons(call):
    is_joined=is_member(call.message)
    if is_joined:
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
                                \n/price:اگر این کامند را بزنی یعنی یک حدود قیمتی می خوای برای محصولی که الان تو ذهنت هست و خب من هم بعد از اینکه محصول  مدنظرت را گفتی اون رنج قیمتش را بهت میگم
                                \n/product:با زدن این کامند و در ادامه با دادن  محصول مدنظر چند تا محصول از آن چیزی که انتخاب کردی را برات می فرستم
                                \n/about:با زدن این کامند اطلاعاتی در خصوص من و توسعه دنده من دریافت می کنی🙈
                                \n/support:برای ارتباط با پشتیبانم فقط لازمه این کامند را بزنی😎
                                \n/guide:اینم از کامند راهنما هستش،می خوای اینو بزنییی؟خب من که الان راهنماییت کردم😐
                                """) 
        
        if call.data=="product":
            user_status[call.message.chat.id]="product"
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="""خب پس چرا معطلی؟!😭
                                \nقصد خرید چه محصولی را داری؟
                                \nاسم آن را برام بنویس
                                """)
        
        if call.data=="avg":
            user_status[call.message.chat.id]="avg"
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="""راجب چه محصولی می خوای رنج قیمتیش را بدونی؟🤓
                                \nآن محصول را برام بنویس
                                """)
            
        if call.data=="support":
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="""اوه، اوه😬
                                \n مثل اینکه کار ضروری برات پیش اومده که با پشتیبانم کار داری
                                \nاین ID پشتیبانم در تلگرام هستش
                                \n@sb_mohsen""")


# command guide
@bot.message_handler(commands=['guide'])   
def get_guide(message):
    bot.send_message(chat_id=message.chat.id,
                                text="""خب ظاهرا به یکم راهنمایی نیاز داری برای کار کردن با من🧐
                                \n/price:اگر این کامند را بزنی یعنی یک حدود قیمتی می خوای برای محصولی که الان تو ذهنت هست و خب من هم بعد از اینکه محصول  مدنظرت را گفتی اون رنج قیمتش را بهت میگم
                                \n/product:با زدن این کامند و در ادامه با دادن  محصول مدنظر چند تا محصول از آن چیزی که انتخاب کردی را برات می فرستم
                                \n/about:با زدن این کامند اطلاعاتی در خصوص من و توسعه دنده من دریافت می کنی🙈
                                \n/support:برای ارتباط با پشتیبانم فقط لازمه این کامند را بزنی😎
                                \n/guide:اینم از کامند راهنما هستش،می خوای اینو بزنییی؟خب من که الان راهنماییت کردم😐
                                """) 

# command about
@bot.message_handler(commands=['about'])   
def get_about(message):
    bot.send_message(chat_id=message.chat.id,
                                text="""خب دوست من همونطور که قبلا اشاره کرده بودم من ربات دیوار هستیم
                                \nوظیفه من این است که برای اینکه شما راحت باشی و لازم نباشه بری تو گوگل و دیوار را سرچ کنی و...
                                \nآقا جان من اینجام😅
                                \nغصه چی را می خوری؟😁
                                \nفقط لب ترک کن و دیتایی که از دیوار می خوای را به من بگو تا بهت تحویل بدم🔥
                                \nکسی که من را ساخته اسمش محسن سرابی هستش البته بگم هااا زیاد باهاش حال نمی کنم😒
                                \nولی خب با این حال اگر خواستی به پورتفولیو آن یک سر بزن، بچه بدی نیست😜
                                \nhttps://www.mhsrbi.ir/
                                """)


# command support
@bot.message_handler(commands=['support'])   
def get_support(message):
    bot.send_message(chat_id=message.chat.id,text="""اوه، اوه😬
                                \n مثل اینکه کار ضروری برات پیش اومده که با پشتیبانم کار داری
                                \nاین ID پشتیبانم در تلگرام هستش
                                \n@sb_mohsen""")    

# command avg
@bot.message_handler(commands=['avg'])   
def get_average(message):
    is_joined=is_member(message)
    if is_joined:
        user_status[message.chat.id]="avg"
        bot.send_message(chat_id=message.chat.id,text="""راجب چه محصولی می خوای رنج قیمتیش را بدونی؟🤓
                                \nآن محصول را برام بنویس
                                """)     

# command products
@bot.message_handler(commands=['product'])   
def get_average(message):
    is_joined=is_member(message)
    if is_joined:
        user_status[message.chat.id]="product"
        bot.send_message(chat_id=message.chat.id,text="""خب پس چرا معطلی؟!😭
                                \nقصد خرید چه محصولی را داری؟
                                \nاسم آن را برام بنویس
                                """)     
    

# structure of getting latest products and avg
@bot.message_handler(func=lambda message:is_member(message))
def get_product_info(message):
    chat_id=message.chat.id
    query = message.text.strip()

    state=user_status[chat_id]
    if state=="product":
        bot.reply_to(message,f"🔎 چند لحظه صبر کن\n  دارم دنبال {query} در سایت دیوار می گردم...")
        results = get_products(query)
        if results:
            response = "\n\n".join(results)
        else:
            response = "❌ چیزی پیدا نشد"

        bot.send_message(message.chat.id, response)
    
        del user_status[chat_id]
    
    elif state=="avg":
        bot.reply_to(message, f"📊چند لحظه صبر کن\n دارم حدود قیمت {query} درمیارم...")
        avg_price = get_avg_price_from_divar(query)
        if avg_price:
            response = f"💰 ببین حدود قیمت {query}، {avg_price:,} تومان هستش"
        else:
            response = "❌ قیمتی پیدا نشد"
        bot.send_message(chat_id, response)

        del user_status[chat_id]

    else:
        bot.send_message(chat_id, "عزیزم ما را گیج کردی😅\n لطفا معلوم کن که میانگین را می خوای یا آخرین محصولات را")


bot.infinity_polling()