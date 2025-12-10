from aiogram import Router , types
from aiogram.filters import CommandStart,Command
from keyboards import create_info_kb_markup

from keyboards import (
    create_info_kb_builder,
    create_info_kb_markup,
)

router=Router()

@router.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        f"Добро  пожаловать, {message.from_user.full_name}",
        reply_markup=create_info_kb_markup(),
    )


@router.message(Command("info", prefix="!/"))
async def handle_info(message: types.Message):
    await message.answer(
        text="Этот бот создан для перевода слов",
    )