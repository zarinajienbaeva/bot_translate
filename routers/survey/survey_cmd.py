from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Survey(StatesGroup):
    
    from aiogram import Router, types
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query()
async def lang_selected(
    callback: types.CallbackQuery, 
    state: FSMContext):
    # faqat kerakli callback_data ni tekshiramiz
    if callback.data not in ["uz_ru", "ru_uz", "en_uz", "uz_en"]:
        return  # boshqa tugmalar uchun hech narsa qilmaymiz

    await state.update_data(lang=callback.data)
    await callback.message.answer(f"Til tanlandi: {callback.data}")
    await callback.answer()
