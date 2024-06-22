import os
import random
from aiogram import Router, types
from aiogram.types import BufferedInputFile

random_image_router = Router()


@random_image_router.callback_query(lambda c: c.data == "random")
async def random_image_handler(callback_query: types.CallbackQuery):
    images_folder = 'images'
    images = os.listdir(images_folder)
    if images:
        random_image = random.choice(images)
        image_path = os.path.join(images_folder, random_image)
        caption = f"Enjoy this dish: {random_image.split('.')[0].replace('_', ' ').title()}"

        # Open the file and read its content
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()

        # Create an instance of BufferedInputFile
        input_file = BufferedInputFile(image_content, filename=random_image)
        await callback_query.message.answer_photo(photo=input_file, caption=caption)
    else:
        await callback_query.message.answer("No images available.")

    await callback_query.answer()
