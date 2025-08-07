import telebot
import requests
from flask import Flask, request

# Use your real token
BOT_TOKEN = "8279689199:AAEc83YTmN0xgA3E-qgasizvDt9JMUv_h4g"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

@app.route("/" + BOT_TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot is running!")

# To keep alive
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
