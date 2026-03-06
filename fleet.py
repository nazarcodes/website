import asyncio
from telegram import Bot

BOT_TOKEN = "8574772148:AAHGGK7VDztbqMt_c9O9nnOJW4YVUcO6WqM"
CHAT_ID = "-1003762231882"

MESSAGE = """
ATTENTION ❗️❗️❗️

Drive safe please. Don't drive if you're tired. Avoid harsh turns or sudden braking, and stay within the speed limit. Keep a safe distance from other cars, stay focused on the road, and take breaks if you feel sleepy. Your safety matters.

SAFETY is of the highest importance.
"""

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    while True:
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
        print("Message sent!")
        await asyncio.sleep(2 * 60 * 60)  # 2 hours in seconds

if __name__ == "__main__":
    asyncio.run(send_message())
