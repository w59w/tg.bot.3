
from aiogram import Router, types


menu_router = Router()


@menu_router.callback_query(lambda c: c.data == "menu")
async def menu_handler(callback_query: types.CallbackQuery):
    menu_text = ("Наше меню:\n"
                 "1. Стейк - 200 сом\n"
                 "2. Лазанья - 200 сом\n"
                 "3. Шашлык - 200 сом\n")
    await callback_query.message.answer(menu_text)
    await callback_query.answer()
