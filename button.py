from telebot import types

checkbutton = types.InlineKeyboardMarkup(row_width=1)
checkbutton.add(
    types.InlineKeyboardButton(text="1-Kanal", url="https://t.me/withlovenabi"),
    types.InlineKeyboardButton(text="Tekshirish ✅", callback_data="checksub")
)