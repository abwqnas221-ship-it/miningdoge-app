import os
import telebot
from telebot import types
from urllib.parse import quote

# ==============================================================================
# 🤖 كود البوت لتشغيل الـ Mini App
# ==============================================================================

# يمكنك استبدال التوكين مباشرة هنا أو تعيينه كـ Environment Variable
BOT_TOKEN = '8924590318:AAFocUkWyI2vEj8PQBroxxVXYCfrp-ac-ao'

# رابط تطبيق الـ Mini App المرفوع على GitHub Pages
WEB_APP_URL = 'https://abwqnas221-ship-it.github.io/miningdoge-app/'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """إرسال القائمة الرئيسية ورابط الـ Mini App"""
    user_name = message.from_user.first_name
    
    welcome_text = (
        f"مرحباً بك **{user_name}** في بوت **MiningDoge VIP** 🚀\n\n"
        "ابدأ الآن بتعدين عملة DOGE مجاناً، واجمع الأرباح اليومية، وقم بترقية أجهزتك لزيادة سرعة التعدين!\n\n"
        "اضغط على زر **\"بدء التعدين الآن 💰\"** بالأسفل لفتح التطبيق."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # 1. زر فتح الـ Mini App داخل التليجرام
    btn_start = types.InlineKeyboardButton(
        text="💰 💰 💰 بدء التعدين الآن 💰 💰 💰", 
        web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    
    # 2. زر دعوة الأصدقاء
    bot_info = bot.get_me()
    ref_link = f"https://t.me/{bot_info.username}?start=ref_{message.from_user.id}"
    share_text = quote("انضم معي لتعدين عملة DOGE مجاناً واكسب أرباحاً يومية! 🚀")
    share_url = f"https://t.me/share/url?url={ref_link}&text={share_text}"
    
    btn_invite = types.InlineKeyboardButton(
        text="🔥 🔥 🔥 دعوة الأصدقاء للحصول على مكافآت 🔥 🔥 🔥", 
        url=share_url
    )
    
    markup.add(btn_start, btn_invite)

    bot.send_message(
        message.chat.id, 
        welcome_text, 
        parse_mode="Markdown", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("🤖 MiningDoge VIP Bot is running...")
    bot.infinity_polling()
