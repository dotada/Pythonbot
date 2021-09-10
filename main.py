import os
import keep_alive
import random
import discord
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
async def rickroll(ctx):
  await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

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
async def r(ctx):
  b = random.randint(0000000, 4480000)
  number = str(b)
  url = "https://rule34.xxx/index.php?page=post&s=view&id=" + number
  await ctx.send(url)

@bot.command()
async def e(ctx):
  v = random.randint(0000000, 2500000)
  y = str(v)
  url2 = "https://e621.net/posts/" + y
  await ctx.send(url2)

@bot.command()
async def b(ctx):
  n = random.randint(0000000, 6100000)
  k = str(n)
  url3 = "https://e926.net/posts/" + k
  await ctx.send(url3)

@bot.command()
async def za(ctx):
  await ctx.send("warudo")

@bot.command()
async def star(ctx):
  await ctx.send("platinum")

@bot.command()
async def nh(ctx):
  g = random.randint(0o00002, 366000)
  o = str(g)
  url4 = "https://nhentai.to/g/" + o
  await ctx.send(url4)

@bot.command()
async def tf(ctx):
  await ctx.send("https://cdn.discordapp.com/emojis/804496731529281563.png?v=1")

@bot.command()
async def cunt(ctx):
  await ctx.send(file=discord.File("cunt.mp3"))

keep_alive.keep_alive()
bot.run(TOKEN)