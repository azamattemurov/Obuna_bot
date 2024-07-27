import time
from telebot import TeleBot, types

token = '7460636843:AAE5k7ZKL8_tWgALM-Y2sZMQ3EyXIpkF83w'
bot = TeleBot(token)
channel = "@t1murov_19"

audio_file = 'music/Ne sabab.mp3'


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("1-Kanal", url="https://t.me/t1murov_19")
    button2 = types.InlineKeyboardButton("Tasdiqlash ✅", callback_data="checksub")
    markup.add(button1, button2)
    bot.send_message(msg.chat.id, "Kanalimizga obuna bo'ling va O'ylab ko'rni - 2 ni eshiting 🔊", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'checksub')
def callback_check_subscription(call: types.CallbackQuery):
    try:
        checkuser = bot.get_chat_member(channel, call.from_user.id).status
        if checkuser in ['member', 'administrator', 'creator']:
            time.sleep(3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Tasdiqlaganingiz uchun rahmat 🥳 \n "
                                       "Sizga 10 soniyada premyera tashlanadi ⏳", reply_markup=None)
            time.sleep(4)
            bot.send_audio(call.message.chat.id, audio=open(audio_file, 'rb'), protect_content=True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_message(call.message.chat.id,
                             "Hozircha Ne sabab ni eshitib turishingiz mumkin hali chiqmadi 😂 \n"
                             "\nBizdan uzoqlashmang 🫴🏻 https://t.me/t1murov_19",
                             protect_content=True)
        else:
            bot.send_message(call.message.chat.id,
                             "Siz hali kanalimizga obuna bo'lmadingiz. Obuna bo'ling va qayta tasdiqlang.",
                             protect_content=True)
    except Exception as e:
        bot.send_message(call.message.chat.id, "Xatolik yuz berdi: {}".format(str(e)), protect_content=True)


@bot.message_handler(content_types=['document', 'photo', 'video'])
def handle_unsupported_content(msg: types.Message):
    bot.send_message(msg.chat.id, "Bu turdagi fayllarni qabul qilmayman. Faqat audio fayl yuboriladi.", protect_content=True)


bot.polling()
