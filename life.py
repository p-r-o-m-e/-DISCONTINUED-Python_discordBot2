import os
from pyexpat.errors import messages
import discord
import asyncio
# from replit import db
from datetime import date
import random
import pickledb


from dotenv import load_dotenv
# from ds import *

db = pickledb.load('e.db', False)

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

imgdisco = "https://i.imgur.com/rvkwqER.jpg"

prefix = ":V"
bot = discord.Client()
print("running")


#dict_names
# "userid"

#db
def oneTimef():
  pass

def dbdump():
  db.dump()
#add tuple to dictionary
def aD(dname, v, v2):
  db.dadd(dname, (str(v),str(v2)))
def setDval(dname,v, v2):
  db.dpop(dname,str(v))
  aD(dname, v, v2)
def getDvalist(dname, v):
  return db.dget(dname, str(v)).split(".")

#db.dget(dict,'name')

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
          # try:
          #     user = db.get('str(message.author.id)')
          #     print(user)
          # except KeyError:
          #   await message.channel.send(f"You're a new face! `{prefix}start` to play or `{prefix} help` for info. {message.author.mention}")
          # else:
          #   await message.channel.send(f"You can use ``` {prefix} help ``` for info! {message.author.mention}")
          if db.dexists(name = "userid" , key = str(message.author.id)) == True:
              await message.channel.send(f"You can use ``` {prefix} help ``` for info! {message.author.mention}")
          else:
              await message.channel.send(f"You're a new face! `{prefix}start` to play or `{prefix} help` for info. {message.author.mention}")


        con = message.content
        con = con.split(" ", 2)
        # pref = con1.startswith(f"{prefix.lower()} ") or con1.startswith(f"{prefix} ")
        # p = (prefix.lower()  , prefix.upper())
        if con[0].upper() == prefix.upper():
            # con = con1.split(" ", 2)
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
              if (db.dexists(name = "userid", key = str(message.author.id)) == False):
              #    user =  db.get('str(message.author.id)')
              #    print(user)
              # except KeyError:

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
                  msg = f"Hello {message.author.name}.\nI work for Discorp inc. And you are a volunteer for our project Disco-Life!\nNow we intend to observe how you live in Disco-Verse, i hope you are ready!" + f"{chr(173)} \n {chr(173)}\n {chr(173)}"

                  today = date.today().strftime("%d-%m-%Y")
                  e =emb("[New] Text Message ", f"`{str(today)}`\n\n" + msg)
                  e.set_author(name = "Agent Disco", url = "", icon_url = imgdisco)
                  cash = 4 * (10 * random.randint(1,8))
                  e.set_footer(text = f"{cash}$ credited to bank account")

                  await message.channel.send(embed=e)
                  await message.channel.send(f" `use {prefix.lower()} action ok` ")

                  try:
                    del msg
                    def check(m):
                      m1=m
                      m = m.content.split(" ", 2)
                      return (m[0].lower() == prefix.lower() and m[1] == "action" and m[2] == "ok") and m1.channel == message.channel and m1.author == message.author
                    msg = await bot.wait_for('message', check=check)

                  except asyncio.exceptions.TimeoutError:
                    await message.channel.send("`TimeOutError`")
                  else:
                    await message.channel.send(f">>> Profile created!{prefix.lower()} profile and many other commands unlocked.")

            elif con == "action":
              if not message.content.split(" ", 2)[2] in getDvalist("user_actions", message.author.id):
                 await message. channel.send("`Err : Invalid command.`")
            else:
                
                await message. channel.send("`Err : Invalid command.`")





bot.run(TOKEN)
