import time
from telebot import TeleBot, types

# Bot token va kanal nomini o'zgartiring
TOKEN = '7832435136:AAH100TOWQqq09BgWqWDM9l6X3-rw2vz5Tw'
CHANNEL_USERNAME = "@T1murov_19"
YOUTUBE_LINK = "https://linktw.in/reVyqY"  # YouTube havolasi

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    channel_button = types.InlineKeyboardButton("📢 Kanalga obuna bo'ling", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
    check_button = types.InlineKeyboardButton("✅ Tasdiqlash", callback_data='check_subscription')
    markup.add(channel_button, check_button)

    bot.send_message(
        message.chat.id,
        "Ber Habar premyerani eshitish uchun 👇🏻 \n\n📢 Iltimos, kanalimizga obuna bo'ling va tasdiqlash tugmasini bosing.",
        reply_markup=markup
    )

# Obuna holatini tekshirish va natijani yuborish
@bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
def check_subscription(call):
    try:
        user_status = bot.get_chat_member(CHANNEL_USERNAME, call.from_user.id).status
        if user_status in ['member', 'administrator', 'creator']:
            # Agar obuna bo'lgan bo'lsa
            bot.edit_message_text(
                "✅ Tasdiqlash muvaffaqiyatli!\n\nMana shu link da Premyera 👇🏻",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=None
            )
            bot.send_message(call.message.chat.id, f" {YOUTUBE_LINK}")
        else:
            # Agar obuna bo'lmagan bo'lsa
            ask_to_subscribe(call.message)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ Xatolik yuz berdi: {e}")

# Obuna bo'lmaganlarga xabar yuborish
def ask_to_subscribe(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    channel_button = types.InlineKeyboardButton("📢 Kanalga o'tish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
    check_button = types.InlineKeyboardButton("✅ Qayta tasdiqlash", callback_data='check_subscription')
    markup.add(channel_button, check_button)

    bot.edit_message_text(
        "❌ Siz hali kanalimizga obuna bo'lmadingiz.\n\n📢 Iltimos, obuna bo'ling va qayta tasdiqlash tugmasini bosing.",
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=markup
    )

# Botni ishga tushirish
while True:
    try:
        bot.polling(timeout=20, long_polling_timeout=20)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        time.sleep(15)
