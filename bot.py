import discord
from unidecode import unidecode
from TOKEN import TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# from functions import *
# from globalVar import *

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mess = unidecode(message.content)
    
    await message.channel.send(mess)


client.run(TOKEN)