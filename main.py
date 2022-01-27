import os
import discord
from replit import db
# from dotenv import load_dotenv
# from ds import *

# load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]

prefix = ":D"
bot = discord.Client()
print("running")

# @bot.event()
# async def on_message(message):
#     if bot.user.mentioned_in(message):
#         await message.channel.send(" `try :D help` ")

def emb(t,desc="", col = 0x3AABC2):
        embedVar = discord.Embed(title=t, description=desc, color=col)
        return embedVar

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if bot.user.mentioned_in(message):
          await message.channel.send(f"You can use ``` {prefix} help ``` for info! {message.author.mention}")
        con1 = message.content
        if con1.startswith(f"{prefix.lower()} ") or con1.startswith(f"{prefix} "):
            con = con1.split(" ", 1)
            con = con[1]
            if con == "quittt":
                    await message.channel.send("``` shutting down ```")
                    exit()
            elif con == "ping":
                await message.channel.send("pong!")
            elif con == "help":
              e=emb(f"**For more info:** ``` {prefix} help [command] ```", f"**Add ``` {prefix} ``` before any command**")
              e.set_author(name="Commands", url="", icon_url="https://image.freepik.com/free-vector/blue-pencil-with-pixel-art-style_475147-504.jpg")
              em = lambda a,b : e.add_field(name=a,value=f"``` {b} ```", inline=False)
              em("\a","\a")
              em(":notebook_with_decorative_cover: Profile commands :notebook_with_decorative_cover:", "start, profile, attributes, boosts, cv")
              em("\a","\a")
              em(":notebook: Menu commands :notebook:", "bank, shop")
              # e.add_field(name="Field1", value="hi", inline=False)
              # e.add_field(name="Field2", value="hi2", inline=False)
              await message.channel.send(embed=e)
                
                
            else:
                pass
    




bot.run(TOKEN)
