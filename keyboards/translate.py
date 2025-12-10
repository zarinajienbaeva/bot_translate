from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from routers import router

@router.message()
async def translate_choose_lang(message: types.Message):
    if message.text != "Tarjima qilish":
        return
    
@router.callback_query()
async def lang_selected(callback: types.CallbackQuery):
    if callback.data not in ["uz","qar","en","ru"]:
        return
    await callback.message.answer(f"Til tanlandi: {callback.data}\nMatnni kiriting:", reply_markup=switch_kb())
    await callback.answer()