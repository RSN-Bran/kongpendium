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

    elif message.content.lower().startswith("!newkong "):
        newKong = message.content.replace("!newkong ", "")
        kongAdded = kongbot.addKong(newKong+"\n")
        if kongAdded:
            await message.channel.send("New Kong just dropped")
        else:
            await message.channel.send("Duplicate Kong Detected")
    elif message.content.lower() == "!allkong":
        await message.channel.send('All Kongs', file=discord.File("kongpendium.txt"))
    elif message.content.lower() == "!help":
        await message.channel.send("Kongmands:\n!kong - Gives a random kong\n!newkong <kong> - adds a new kong to the list\n!allkong - provides a text file with all kongs\n!help - you are looking at it")

    

client.run(TOKEN)