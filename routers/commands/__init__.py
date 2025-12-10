from aiogram import Router
from .info_cmd import router as info_router
#from .text_handlers import router as text_router
router = Router()

router.include_routers(
    info_router,
   # text_router,
)