import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "💗 Welcome to FIC RANDOMIZER!\n\n"
        "Generate a random idea for your next fanfic."
    )


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    