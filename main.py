import os
import discord
from dotenv import load_dotenv
from ds import *

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

prefix = ":D"
bot = discord.Client()
print("running")

# @bot.event()
# async def on_message(message):
#     if bot.user.mentioned_in(message):
#         await message.channel.send(" `try :D help` ")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        con1 = message.content
        if con1.startswith(f"{prefix} "):
            con = con1.split(" ", 1)
            con = con[1]
            if con == "quittt":
                    await message.channel.send("``` shutting down ```")
                    exit()





bot.run(TOKEN)
