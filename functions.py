import discord
from unidecode import unidecode
from client import client

# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    
# Called whenever message is send on any channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mess = unidecode(message.content)
    
    await message.channel.send(mess)
    
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel == None and after.channel != None:
        print(member)
