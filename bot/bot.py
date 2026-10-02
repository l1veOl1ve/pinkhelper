import asyncio
import json
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from openai import AsyncOpenAI

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL") # https://l1ve01ve.github.io/pinkhelper/web/
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

ai_client = AsyncOpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хранилище контекста игры
GAME_DATA_FILE = "data/game_context.json"
os.makedirs("data", exist_ok=True)

def load_game_data():
    if os.path.exists(GAME_DATA_FILE):
        with open(GAME_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"characters": [], "plot": "", "history": []}

def save_game_data(data):
    with open(GAME_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@dp.message(CommandStart())
async def start_handler(message: Message):
    # Кнопки для открытия двух разных Mini App
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✦ FIC RANDOMIZER ✦",
                    web_app=WebAppInfo(url=f"{WEB_APP_URL}index.html")
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎮 GAME DEV COMPANION 🎮",
                    web_app=WebAppInfo(url=f"{WEB_APP_URL}game.html")
                )
            ]
        ]
    )

    await message.answer(
        "🌸 **Pink Helper Workspace**\n\n"
        "Выберите инструмент:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# Обработка данных, отправленных из game.html через tg.sendData()
@dp.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    game_data = load_game_data()
    payload = json.loads(message.web_app_data.data)
    action = payload.get("action")
    text = payload.get("text")

    if action == "add_character":
        game_data["characters"].append(text)
        save_game_data(game_data)
        await message.answer(f"✅ **Персонаж добавлен в память AI:**\n{text}")

    elif action == "update_plot":
        game_data["plot"] = text
        save_game_data(game_data)
        await message.answer(f"📝 **Сюжет обновлен:**\n{text}")

    elif action == "ask_ai":
        await message.answer("🧠 *AI думает...*", parse_mode="Markdown")
        
        system_prompt = f"""
        Ты ассистент по разработке игры на Unreal Engine 5 и Blender.
        Сохраненные персонажи: {json.dumps(game_data['characters'], ensure_ascii=False)}
        Текущий сюжет/прогресс: {game_data['plot']}
        
        Помогай с логикой, кодом, развитием сюжета и персонажей.
        """

        if ai_client:
            response = await ai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ]
            )
            answer = response.choices[0].message.content
            await message.answer(f"🤖 **Ответ AI:**\n\n{answer}", parse_mode="Markdown")
        else:
            await message.answer("⚠️ OPENAI_API_KEY не указан в .env")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())