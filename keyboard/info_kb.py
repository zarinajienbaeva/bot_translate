from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

def create_info_kb_markup():
    btn1 = KeyboardButton(text="Tarjima qilish")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [btn1]
        ],
        resize_keyboard=True,
    )
    return keyboard