import discord
from unidecode import unidecode
from time import sleep
from client import client
from globalVar import *

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
    
    if member == client.user:
        return
    
    if before.channel == None and after.channel != None:
        guild = after.channel.guild
        print(member)
        await guild.change_voice_state(channel=after.channel)
        sleep(10)
        await guild.change_voice_state(channel=None)

