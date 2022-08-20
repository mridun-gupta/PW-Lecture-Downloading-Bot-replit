import os
from pyrogram import Client as c, filters
from pyrogram.types import *
from pyromod import listen
def cloudfront_WORK(m):
        try:
         link = m.command[1]
         os.system(f'youtube-dl -o cloudfront.mp4 "{link}"')
         bot.send_video(m.chat.id, "cloudfront.mp4")
         os.remove("cloudfront.mp4")
        except:
          m.reply("Link could not be found!")
        del cloudfront_TASK[0]
def youtube_WORK(m):
    try:
     link = m.command[1]
     os.system(f'youtube-dl -o youtube.mp4 -f best "{link}"')
     bot.send_video(m.chat.id, "youtube.mp4")
     os.remove("youtube.mp4")
    except:
          m.reply("Link could not be found!")
    del youtube_TASK[0]
cloudfront_TASK = []
youtube_TASK = []
LOG = -1001369097733
API_ID = 13633869
API_HASH = "45080180db98637def8696d84eddfcef"
BOT_TOKEN = "5492506998:AAEo_qbEXjbgZqxl4H_i0fRd5Jg7wJa9c_A"
bot = c("PW Lecture DL Bot", API_ID, API_HASH, BOT_TOKEN)
@bot.on_message(filters.command("start"))
async def starting(c: bot, m: Message):
    await m.reply("Hey! Welcome, which lecture do you want to download today?\nMake use of 'convert' and 'download' command to download your video lecture.\n\nThere might be some delay get your request fulfilled due to server's heavy usage by users simultaneously.")
@bot.on_message(filters.command("cloudfront"))
async def making(c: bot, m: Message):
    await m.reply("Paste the video lecture's link after the command, and the bot will start downloading the video lecture in background, and, just sit back and enjoy!")
    await bot.send_message(LOG, "Got a CloudFront DL task by "+m.from_user.id +"\n\nThe Text was "+m.text)
    cloudfront_TASK.append(m)
    if len(cloudfront_TASK) ==1:
      cloudfront_WORK(cloudfront_TASK[0])
      if len(cloudfront_TASK)> 0:
        cloudfront_WORK(cloudfront_TASK[0])
@bot.on_message(filters.command("youtube"))
async def making(c: bot, m: Message):
  await m.reply("Paste the video lecture's link after the command, and the bot will start downloading the video lecture in background, and, just sit back and enjoy!")
  await bot.send_message(LOG, "Got a CloudFront DL task by "+m.from_user.id +"\n\nThe Text was "+m.text)
  youtube_TASK.append(m)
  if len(youtube_TASK) ==1:
      youtube_WORK(youtube_TASK[0])
      if len(youtube_TASK)> 0:
        youtube_WORK(youtube_TASK[0])
bot.run()