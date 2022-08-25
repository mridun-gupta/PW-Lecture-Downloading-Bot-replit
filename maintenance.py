from pyrogram import Client as c, filters
from pyrogram.types import *
API_ID = 13633869
API_HASH = "45080180db98637def8696d84eddfcef"
BOT_TOKEN = "5492506998:AAEo_qbEXjbgZqxl4H_i0fRd5Jg7wJa9c_A"
bot = c("PW Lecture DL Bot", API_ID, API_HASH, BOT_TOKEN)
@bot.on_message(filters.command(["start", "cloudfront", "youtube"])) #easier_way
async def starting(c: bot, m: Message):
  await m.reply("Hey! Welcome, Bot is under maintenance!\n\nWhat's New:\n > Bug Fixing")
@bot.on_message(filters.command(["bitgravity"]))
async def starting(c: bot, m: Message):
  await m.reply("Hey! Welcome, this module is getting tested! COMING VERY SHORTLY!")
bot.run()