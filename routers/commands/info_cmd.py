from aiogram import Router , types
from aiogram.filters import CommandStart,Command

router=Router()

@router.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        f"Добро  пожаловать, {message.from_user.full_name}",
    )


@router.message(Command("info", prefix="!/"))
async def hanle_info(message: types.Message):
    await message.answer(
        text="Этот бот создан для перевода слов",
    )