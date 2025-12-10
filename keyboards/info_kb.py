from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def create_info_kb_markup():
    btn1 = KeyboardButton(text="Tarjima qilish")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [btn1]
        ],
        resize_keyboard=True,
    )
    return keyboard
def create_info_kb_builder():
    builder = ReplyKeyboardBuilder()
    for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
        builder.button(
            text=f"Set {i}",
        )
    builder.adjust(1)
    return builder.as_markup()

def create_m_info_kb_markup() :
    btn2 = KeyboardButton(text="til almastiriw")
    btn3 = KeyboardButton(text="artqa qaytiw")
    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [btn2],
            [btn3]
        ],
        resize_keyboard=True,
    )
    return keyboard
