from aiogram import Bot,Dispatcher,F
from googletrans import Translator
from config import token
from routers import router
import asyncio


my_bot = Bot(token=str(token))
dp = Dispatcher()
translator = Translator()

async def main():
    print("I am starting ...")
    dp.include_router(router)
    await dp.start_polling(my_bot)

if __name__ == "__main__":
    asyncio.run(main())