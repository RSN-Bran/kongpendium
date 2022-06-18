import discord
import kongbot
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print("Kongbot online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Supply a random kong
    if message.content.lower().startswith("!kong"):
        response = kongbot.randomKong().strip()
        await message.channel.send(response)

    elif message.content.lower().startswith("!newkong ") or message.content.lower().startswith("!addkong "):
        command = ""
        if("!newkong " in message.content):
            command = "!newkong "
        elif("!addkong " in message.content):
            command = "!addkong "
        newKong = message.content.replace(command, "")
        kongAdded = kongbot.addKong(newKong+"\n")
        if kongAdded:
            await message.channel.send("New Kong just dropped")
        else:
            await message.channel.send("Duplicate Kong Detected")

    elif message.content.lower() == "!allkong":
        await message.channel.send('All Kongs', file=discord.File("kongpendium.txt"))

    elif message.content.lower().startswith("!similarkong "):
        similarKong = message.content.replace("!similarkong ", "")
        similarKongs = kongbot.similarKong(similarKong)
        print(similarKongs)
        await message.channel.send("These are the closest kongs:\n" + ''.join(similarKongs))

    elif message.content.lower() == "!help":
        helpfile = open("help.txt", "r")
        await message.channel.send(helpfile.read())
        helpfile.close()

    

client.run(TOKEN)