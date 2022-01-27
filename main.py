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
              
              space = "\a\n\a"
              em = lambda a,b,c="" : e.add_field(name=a,value=f"``` {b} ```{c}", inline=False)
           
              em(f"{space}:bookmark: Profile commands :bookmark:", "start, profile, attributes, boosts, cv", space)
              em(":beginner: Menu commands :beginner:", "bank, shop, jobs, education, special", space)
              em(":gift: Rewards commands :gift:", "daily, votetrend, checkin, quiz", space)
              em(":currency_exchange: Interaction commands :currency_exchange:", "give, phone", space)
              em(":diamonds: Misc commands :diamonds:", "setprefix, msgdev")

              await message.channel.send(embed=e)
                
                
            else:
                pass
    




bot.run(TOKEN)
