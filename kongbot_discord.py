import discord
import kongbot_parse
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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
        await message.channel.send(kongbot_parse.parse(message.content, "discord"))    

client.run(TOKEN)