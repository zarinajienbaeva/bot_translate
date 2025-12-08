from aiogram import F, Router, types
from googletrans import Translator
from config import my_id 

router = Router()
translator = Translator()

@router.message(F.text.from_user.id == my_id)
async def translate_message(message: types.Message):
    result = translator.translate(message.text, dest='en')
    await message.answer(result.text)
