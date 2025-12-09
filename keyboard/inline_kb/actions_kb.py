from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def build_actions_kb():
    btn1 = InlineKeyboardButton(
        text="Uz-Ru",
        callback_data="uz_ru",
    )
    btn2 = InlineKeyboardButton(
        text="Uz-En",
        callback_data="uz-en",
    )
    btn3 = InlineKeyboardButton(
        text="Ru-En",
        callback_data="ru-en",
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[btn1,btn2], [btn3]],
    )
    return kb

