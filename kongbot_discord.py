import discord
import kongbot_parse
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

    if message.content.lower() == "!allkong":
        await message.channel.send('All Kongs', file=discord.File("kongpendium.txt"))

    else:
        return kongbot_parse.parse(message.content, "discord")
    

client.run(TOKEN)