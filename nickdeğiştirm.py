from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import pytz
from datetime import datetime

ramos = api id gir  
yamo = "api hash gir"  

ramowlf = TelegramClient("ramowlf_bot.session", ramos, yamo)

async def insta_ramowlf():
    amcik = ""
    while True:
        inleme = datetime.now(pytz.timezone("Europe/Istanbul")).strftime("%H:%M")
        if inleme != amcik:
            amcik = inleme
            yarrak = f"RAMAZAN ÖZTÜRK ({amcik})"
            try:
                await ramowlf(UpdateProfileRequest(first_name=yarrak))
                print(f"Güncellendi: {yarrak}")
            except Exception as e:
                print(f"Hata: {e}")  
        await asyncio.sleep(1)

async def bb():
    await ramowlf.start()  
    await insta_ramowlf()

with ramowlf:
    ramowlf.loop.run_until_complete(bb())  