import os
import discord
import asyncio
from replit import db
# from dotenv import load_dotenv
# from ds import *

# load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]

prefix = ":V"
bot = discord.Client()
print("running in " +  str(len(bot.guilds)) + " servers!")

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
              e=emb(f"**For more info:** ` {prefix} help [command] `", f"**Add ` {prefix} ` before any command**")
              e.set_author(name="Commands", url="", icon_url="https://image.freepik.com/free-vector/blue-pencil-with-pixel-art-style_475147-504.jpg")

              def em(a, b, c=""):
                st = "" 
                for s in b:
                  st += f"`{s}`, " 
                st= st[:-2] + st[-1:]

                return e.add_field(name=chr(173) + "\n" + chr(173) + a,value=f"{st} {c}", inline=False)

              em(":bookmark: Profile commands :bookmark:", ("start", "profile", "attributes", "boosts", "events", "likes", "inventory", "cooldowns"))
              em(":beginner: Menu commands :beginner:", ("bank", "shop", "jobs", "education", "health", "apartments", "relationship"))
              em(":gift: Rewards commands :gift:", ("daily", "weekly", "votetrend", "checkin", "redeem", "quiz"))
              em(":currency_exchange: Interaction commands :currency_exchange:", ("mail", "give", "phone"))
              em(":diamonds: Misc commands :diamonds:", ("action", "gameplayinfo", "rules", "noticeboard", "invite","msgdev"))
              await message.channel.send(embed=e)
                
            elif con == 'start':
              user = message.author
              try:
                 user = db["life"]["disco_users"][user]
              except KeyError:
                #  await message.channel.send(e)
                 await message.channel.send(f"Hi {user.mention}!\nMake sure you have read and accepted the rules (`{prefix} rules`).\nif Yes, react with :thumbsup: !")
                #  await bot.add_reaction(accept_decline, emoji="redCross:423541694600970243")

                 try:
                  reaction, user = await bot.wait_for('reaction_add', timeout=15.0)
                 except asyncio.exceptions.TimeoutError:
                    await message.channel.send("`TimeOutError`")
                 else:
                    if (user == message.author):
                      print (reaction)
                      await message.channel.send(f"{reaction}")
                    else:
                      await message.channel.send(f"`Err : Interference by : `{user.mention}")
                      

            else:
                await message. channel.send("`Err : Invalid command.`")  
                




bot.run(TOKEN)
