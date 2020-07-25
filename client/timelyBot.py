from telegram.bot import Bot
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class TimelyBot():
    def __init__(self):
        TOKEN = getenv("TELEGRAMBOT_TOKEN")
        self.bot = Bot(token=TOKEN)

    def sendReminder(self, CHAT_ID: str, MESSAGE: str) -> bool:
        try:
            message = self.bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
            print(f"Sent reminder to {CHAT_ID}")
            return True
        except Exception:
            print("ERROR")
            return False
