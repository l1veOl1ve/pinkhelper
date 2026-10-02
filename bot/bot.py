import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from aiogram.filters import CommandStart

from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)


load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✦ OPEN RANDOMIZER ✦",
                    web_app=WebAppInfo(
                        url=WEB_APP_URL
                    )
                )
            ]
        ]
    )

    await message.answer(
        "💗 <b>FIC RANDOMIZER</b>\n\n"
        "Generate your next fanfic idea!",
        reply_markup=keyboard
    )


async def main():

    logging.basicConfig(
        level=logging.INFO
    )

    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    