import os
import keep_alive
import random
from discord.ext import commands


bot = commands.Bot(command_prefix=';')
TOKEN = os.environ['TOKEN']

@bot.listen("on_message")
async def ea(message):
 if not message.attachments:
  print("message: " + message.content + "," + " " + "Author: {}".format(message.author.name))
 if message.attachments:
   split_v1 = str(message.attachments).split("filename='")[1]
   filename = str(split_v1).split("' ")[0]
   if filename.endswith(".txt"):
    await message.attachments[0].save(fp="files/{}".format(filename))
   if filename.endswith(".mp4"):
     await message.attachments[0].save(fp="files/{}".format(filename))
   if filename.endswith(".png"):
     await message.attachments[0].save(fp="files/{}".format (filename))
   if filename.endswith(".jpg"):
     await message.attachments[0].save(fp="files/{}".format(filename))
   if filename.endswith(".jpeg"):
     await message.attachments[0].save(fp="files/{}".format(filename))       

@bot.command()
async def naix(ctx):
 await ctx.send("gg wp")

@bot.command()
async def test(ctx):
 await ctx.send("tinyurl.com/heckerforhire")

@bot.command()
async def error(ctx):
 await ctx.send("""
 ------ BOOT ERRORS DETECTED ------
ERROR: Unable to load system file x-server.sys
ERROR: Locate and restore a valid x-server file in ~/sys/ folder to restore UX functionality
ERROR: Consider examining reports in ~/log/ for problem cause and source
ERROR: System UX resource unavailable -- defaulting to terminal mode
.
.
.
---------------------------------
""")

@bot.command()
async def caniputmyballsinyojaws(ctx):
 await ctx.send("can 'a put ma balls in yo jaws?" + "https://www.youtube.com/watch?v=Ik_ZPUbnEJs&t=136s&ab_channel=Ghostgayaya")

@bot.command()
async def DBH(ctx):
 await ctx.send("28 STAB WOUNDS" + "," + " " + "28 ударов ножом")

@bot.command()
async def life(ctx):
 await ctx.send("if you see this, im alive")

@bot.command()
async def cursed(ctx):
  await ctx.send("https://www.youtube.com/watch?v=icmcr0mDgLk")

@bot.command()
async def inspect(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/885182840738816001/885308611079847976/Screenshot_1625.png")

@bot.command()
async def r34(ctx):
  b = random.randint(0000000, 4480000)
  number = str(b)
  url = "https://rule34.xxx/index.php?page=post&s=view&id=" + number
  await ctx.send(url)

keep_alive.keep_alive()
bot.run(TOKEN)