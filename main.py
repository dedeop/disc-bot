import os
from dotenv import load_dotenv
import discord

load_dotenv()

api_key = os.getenv("API_KEY")

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('Hi! This is a placeholder message for now. Future planned commands planned include: \n' \
        '- VC compatibility (music bot if possible) \n' \
        '- Moderation capabilities')



client.run(api_key)