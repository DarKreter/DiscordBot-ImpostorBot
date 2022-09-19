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
    
# Called when someone changes their voice state (connects to vc)
@client.event
async def on_voice_state_update(member, before, after):
    
    # ignore ourself
    if member == client.user:
        return
    
    # If someone join channel (not change or deaf)
    if before.channel == None and after.channel != None:
        print(member)
        
        guild = after.channel.guild # Get guild
        await guild.change_voice_state(channel=after.channel) # Change voice state
        voiceConnection = await after.channel.connect() # connect
        
        source = discord.FFmpegPCMAudio("test.mp3") # Get audio file
        voiceConnection.play(source) # play it
        
        # Wait until bot is playing
        while voiceConnection.is_playing():
            sleep(1)
            
        await voiceConnection.disconnect() # disconnect




