import asyncio
import logging
from config import dp, bot
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.random import random_image_router
from handlers.review import review_router


async def main():
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(menu_router)
    dp.include_router(random_image_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
