import os, asyncio
from pyrogram import Client as c, filters
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyromod import listen
async def cloudfront_WORK(m):
  try:
    link = m.command[1]
    os.system(f'yt-dlp --merge-output-format mp4 --output cloudfront "{link}"')
    await bot.send_video(m.chat.id, "cloudfront.mp4")
    os.remove("cloudfront.mp4")
  except:
      await m.reply("Sorry! Invalid Link!")
  del cloudfront_TASK[0]
async def youtube_WORK(m):
  try:
    link = m.command[1]
    os.system(f'yt-dlp --merge-output-format mp4 --output youtube -f best "{link}"')
    await bot.send_video(m.chat.id, "youtube.mp4")
    os.remove("youtube.mp4")
  except:
      await m.reply("Sorry! Invalid Link!")
  del youtube_TASK[0]
async def bitgravity_WORK(m):
  try:
    link = m.command[1]
    os.system(f'yt-dlp --merge-output-format mp4 --output bitgravity "{link}"')
    await bot.send_video(m.chat_id, "bitgravity.mp4")
    os.remove("bitgravity.mp4")
  except:
      await m.reply("Sorry! Invalid Link!")
  del bitgravity_TASK[0]
async def auth(message):
  try:
    user = await bot.get_chat_member(LOG, message.from_user.id)
    if str(user.status).split(".")[1].strip() == "BANNED": #super_easier_code
      await message.reply_text("Sorry! You are banned!")
      authchk=0
  except UserNotParticipant:
    await message.reply("Sorry! You are not Permitted yet!")
    authchk=0
  else:
    authchk=1 #doesnt_matter
  return authchk
cloudfront_TASK = []
youtube_TASK = []
bitgravity_TASK = []
LOG = -1001745914616
API_ID = 13633869
API_HASH = "45080180db98637def8696d84eddfcef"
BOT_TOKEN = "5492506998:AAEo_qbEXjbgZqxl4H_i0fRd5Jg7wJa9c_A"
bot = c("PW Lecture DL Bot", API_ID, API_HASH, BOT_TOKEN)
@bot.on_message(filters.command("start"))
async def starting(c: bot, m: Message):
  await m.reply("Hey! Welcome, which lecture do you want to download today?\nMake use of 'convert' and 'download' command to download your video lecture.\n\n---\nIMPORTANT\n---\n\n > Your actions will be logged at the backend server for security concerns, for next 7 days, it will be cleared off regularly.\n > There might be some delay get your request fulfilled due to server's heavy usage by users simultaneously.")
@bot.on_message(filters.command("cloudfront"))
async def cloudfront(c: bot, m: Message):
 ac = await auth(m)
 if ac !=0: 
  await m.reply("Paste the video lecture's link after the command, and the bot will start downloading the video lecture in background, and, just sit back and enjoy!")
  await bot.send_message(LOG, "NEW TASK!\n"+str(m.from_user.id)+" have registered a new task for file, from Cloudfront.\n\n The command and link provided is\n```"+m.text+"```")
  cloudfront_TASK.append(m)
  if len(cloudfront_TASK) ==1:
    cloudfront_WORK(cloudfront_TASK[0])
  if len(cloudfront_TASK)> 0:
    cloudfront_WORK(cloudfront_TASK[0])
@bot.on_message(filters.command("youtube"))
async def youtube(c: bot, m: Message):
 ac = await auth(m)
 if ac !=0:  
  await m.reply("Paste the video lecture's link after the command, and the bot will start downloading the video lecture in background, and, just sit back and enjoy!")
  await bot.send_message(LOG, "NEW TASK!\n"+str(m.from_user.id)+" have registered a new task for downloading a file, from YouTube.\n\n The command and link provided is\n```"+m.text+"```")
  youtube_TASK.append(m)
  if len(youtube_TASK) ==1:
    youtube_WORK(youtube_TASK[0])
  if len(youtube_TASK)> 0:
    youtube_WORK(youtube_TASK[0])
@bot.on_message(filters.command("bitgravity"))
async def bitgravity(c: bot, m:Message):
 ac = await auth(m)
 if ac !=0:
  await m.reply("Paste the video lecture's link after the command, and the bot will start downloading the video lecture in background, and, just sit back and enjoy!")
  await bot.send_message(LOG, "NEW TASK!\n"+str(m.from_user.id)+" have registered a new task for downloading a file, from BitGravity.\n\nThe command and link provided is\n```"+m.text+"```")
  bitgravity_TASK.append(m)
  if len(bitgravity_TASK)> 0:
    bitgravity_WORK(bitgravity_TASK[0])
bot.run()