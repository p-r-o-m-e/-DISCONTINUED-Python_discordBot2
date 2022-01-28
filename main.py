import os
import discord
import asyncio
from replit import db
from datetime import date

# from dotenv import load_dotenv
# from ds import *

# load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]

prefix = ":V"
bot = discord.Client()
print("running")

#db functions

def addDB(cat, item):
  pass


# -----------------------

def emb(t,desc="", col = 0x3AABC2):
        embedVar = discord.Embed(title=t, description=desc, color=col)
        return embedVar

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    activity = discord.Game(name=f"Disco-Life  | {prefix} help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if bot.user.mentioned_in(message):
          try:
              user = db["life"]["disco_users"][message.author.id]
          except KeyError:
            await message.channel.send(f"You're a new face! `{prefix}start` to play or `{prefix} help` for info. {message.author.mention}")
          else:
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
              u = user = message.author
              try:
                 user = db["life"]["disco_users"][user.id]
              except KeyError:

                 msg = await message.channel.send(f">>> [ boots up ]\n\nYou want to play Disco-Life! \nCheck out gameplayinfo,\nMake sure you have read and\naccepted the rules .\nThen react with :thumbsup: !\n\n`{prefix.lower()} gameplayinfo`, `{prefix.lower()} rules`")
                 await msg.add_reaction(emoji="\N{THUMBS UP SIGN}")

                   #  had an error for so long because of typing - ch(user, reaction) here :(
                 def ch(reaction, user): 
                   return user == u and str(reaction) == "\N{THUMBS UP SIGN}" and reaction.message == msg
                   
                 try:
                  r = await bot.wait_for("reaction_add", timeout=25.0, check = ch)
                  del r
                 except asyncio.exceptions.TimeoutError:
                    await message.channel.send("`TimeOutError`")
                 else:
                  del msg
                  msg = f"Hello {message.author.name}.\nI work for Discorp inc. And you are a product of our project Disco-Life!\nNow we intend to observe how you live in Disco-Verse, i hope you are ready!"

                  today = date.today().strftime("%d-%m-%Y")
                  e =emb("[New] Text Message ", f"`{str(today)}`\n\n" + msg)
                  e.set_author(name = "Agent Disco", url = "", icon_url = "http://clipart-library.com/image_gallery/n829721.jpg")
                  await message.channel.send(embed=e)

            else:
                await message. channel.send("`Err : Invalid command.`")  
                




bot.run(TOKEN)
