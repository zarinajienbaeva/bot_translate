from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def build_actions_kb():
    btn1 = InlineKeyboardButton(
        text="Qar",
        callback_data="qar",
    )
    btn2 = InlineKeyboardButton(
        text="Uz",
        callback_data="uz",
    )
    btn3 = InlineKeyboardButton(
        text="Ru",
        callback_data="ru",
    )
    btn4 = InlineKeyboardButton(
        text="En",
        callback_data="en",
    )
    btn5 = InlineKeyboardButton(
        text="Qar",
        callback_data="qar",
    )
    btn6 = InlineKeyboardButton(
        text="Uz",
        callback_data="uz",
    )
    btn7 = InlineKeyboardButton(
        text="Ru",
        callback_data="ru",
    )
    btn8 = InlineKeyboardButton(
        text="En",
        callback_data="en",
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[btn1,btn2], 
                         [btn3,btn4],
                         [btn5,btn6],
                         [btn7,btn8]
                         ],
    )
    return kb

