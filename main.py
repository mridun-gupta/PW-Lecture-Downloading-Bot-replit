import os
from pyrogram import Client as c, filters
from pyrogram.types import *
from pyromod import listen
API_ID = 13633869
API_HASH = "45080180db98637def8696d84eddfcef"
BOT_TOKEN = "5492506998:AAEo_qbEXjbgZqxl4H_i0fRd5Jg7wJa9c_A"
bot = c("PW Lecture DL Bot", API_ID, API_HASH, BOT_TOKEN)
@bot.on_message
async def starting(c: bot, m: Message):
    await m.reply("Hey! Welcome, Bot is under maintenance!")
bot.run()