import os
import requests
import telebot

TG_TOKEN = os.getenv("TG_API_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
ADS_TOKEN = os.getenv("ADS_API_TOKEN")

bot = telebot.TeleBot(TG_TOKEN)

def get_ads():
    headers = {'Authorization': f'{ADS_TOKEN}'}
    url = 'https://ads-api.ru/main/api?type=rent&category=realty&city=Москва&source=avito&limit=3'
    r = requests.get(url, headers=headers)
    return r.json()

@bot.message_handler(commands=['run'])
def send_ads(message):
    ads = get_ads()
    for ad in ads.get('data', []):
        text = (
            f"🏠 {ad.get('title')}\n"
            f"📍 {ad.get('address')}\n"
            f"💰 {ad.get('price')}\n\n"
            f"{ad.get('description')}\n\n"
            f"🔗 {ad.get('url')}"
        )
        bot.send_message(CHANNEL_ID, text)

bot.infinity_polling(timeout=10, long_polling_timeout=5)
