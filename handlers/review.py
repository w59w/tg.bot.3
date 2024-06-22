from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()


class Recall(StatesGroup):
    name = State()
    contact = State()
    visit_data = State()
    rate_dish = State()
    rate_clean = State()
    comments = State()


@review_router.callback_query(lambda c: c.data == "review")
async def menu_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(Recall.name)
    await callback_query.message.answer("Whats your full name?")
    await callback_query.answer()


@review_router.message(Command("review1"))
async def start_review(message: types.Message, state: FSMContext):
    await state.set_state(Recall.name)
    await message.answer("Whats your full name?")


@review_router.message(Command("stop"))
@review_router.message(F.text == "stop")
async def stop_survey(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Review stopped")


@review_router.message(Recall.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Recall.contact)
    await message.answer("Give us your contact number or social media")


@review_router.message(Recall.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(Recall.visit_data)
    await message.answer("When was the last time you visited our restaurant?")


@review_router.message(Recall.visit_data)
async def process_visit_data(message: types.Message, state: FSMContext):
    await state.update_data(visit_data=message.text)
    await state.set_state(Recall.rate_dish)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Very good")],
            [types.KeyboardButton(text="Good")],
            [types.KeyboardButton(text="Not bad")],
            [types.KeyboardButton(text="Bad")]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Please rate our dishes {message.from_user.first_name}!", reply_markup=kb)


@review_router.message(Recall.rate_dish)
async def process_rate_dish(message: types.Message, state: FSMContext):
    await state.update_data(rate_dish=message.text)
    await state.set_state(Recall.rate_clean)
    kb = types.ReplyKeyboardRemove()
    await message.answer("Please rate the cleanness of our restaurant", reply_markup=kb)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Very nice")],
            [types.KeyboardButton(text="Good")],
            [types.KeyboardButton(text="Not bad")],
            [types.KeyboardButton(text="Bad")]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Please rate our cleanness {message.from_user.first_name}!", reply_markup=kb)


@review_router.message(Recall.rate_clean)
async def process_rate_clean(message: types.Message, state: FSMContext):
    await state.update_data(rate_clean=message.text)
    await state.set_state(Recall.comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer("Write some comments", reply_markup=kb)


@review_router.message(Recall.comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(comments=message.text)
    data = await state.get_data()
    print("Data", data)
    await state.clear()
    await message.answer("Thanks for your review!")
