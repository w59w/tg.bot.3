from aiogram import Router, F, types
from aiogram.filters.command import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Our site", url="https://mypizza.kg/")
            ],
            [
                types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com")
            ],
            [
                types.InlineKeyboardButton(text="About Us", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Donate", callback_data="donate")
            ],
            [
                types.InlineKeyboardButton(text="Our Menu", callback_data="menu")
            ],
            [
                types.InlineKeyboardButton(text="Random Dish", callback_data="random")
            ],
            [
                types.InlineKeyboardButton(text="Review", callback_data="review")
            ]
        ]
    )
    name = message.from_user.first_name
    await message.answer(
        f'Hello, dear{name}!',
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer()  # для того чтобы бот не зависал
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "donate")
async def donate_handler(callback: types.CallbackQuery):
    await callback.answer()  # для того чтобы бот не зависал
    await callback.message.answer("Мы будем очень благодарны за вашу помощь")
