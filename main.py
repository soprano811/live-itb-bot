from flask import Flask
import requests

app = Flask(__name__)

BOT_TOKEN = "8037116362:AAFtX5UVOTWn0yZ_iqlvLFIc6qW1hAGwbNY"
CHAT_ID = 299383189

@app.route("/")
def index():
    send_message("✅ Бот запущен и готов к работе!")
    return "Bot is running."

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if name == "__main__":
    app.run(host="0.0.0.0", port=8080)
