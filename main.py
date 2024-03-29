import telebot
import logging
import config
from gpt import ask_gpt
from database import create

bot = telebot.TeleBot(config.BOT_TOKEN)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="log_file.txt",
    filemode="w",
)

@bot.message_handler(commands=['start'])
def start(message):
    logging.info("Отправка приветственного сообщения")
    bot.send_message(message.chat.id, 'Привет! Я бот с нейросетью Yandex GPT "Лысый". Задай любой вопрос.')
    logging.info("Отправка промта")
    bot.register_next_step_handler(message, prompt)

@bot.message_handler(func=lambda message: True)
def main(message):
    logging.info("Отправка промта")
    prompt(message)

def prompt(message):
    response = ask_gpt(message.text)
    bot.send_message(message.chat.id, response)
    logging.info("Ответ нейронки")
    create(message.text, response)

logging.info("Bot started")
bot.polling()
