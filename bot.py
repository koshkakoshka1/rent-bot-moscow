import os
import requests
import telebot

TG_TOKEN = os.getenv("7781988624:AAGt_4WMEKvTTeOkQH8KaVnr_pCJmTrFb8g")
CHANNEL_ID = os.getenv("1001479655015")
ADS_TOKEN = os.getenv("a1ef5cae14f81917c0fa8040541bdbf2")

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
        text = f"🏠 {ad.get('title')}
📍 {ad.get('address')}
💰 {ad.get('price')}
\n{ad.get('description')}
\n🔗 {ad.get('url')}"
        bot.send_message(CHANNEL_ID, text)

bot.polling()
