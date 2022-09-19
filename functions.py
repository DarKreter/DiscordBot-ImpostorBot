import discord
from unidecode import unidecode
from time import sleep
from client import client
from globalVar import *


async def ChangeUsernameAndAvatar(guildID, user=None):
    guild = client.get_guild(guildID)
    myself  = discord.utils.get(guild.members, id=BOTanID)
    if user == None:
        # Change back to BOTan
        
        await myself.edit(nick=None)
        
        filename = "images/BOTan_avatar.jpg"
        
        fp = open(filename, 'rb')
        pfp = fp.read()
        await client.user.edit(avatar=pfp)
        
    else:
        # Change username based on userID, and guildID
        user    = discord.utils.get(guild.members, id=users[user])
        
        print(user.display_name)
        
        await myself.edit(nick=user.display_name)
        
        # Save profile picture to file
        filename = "images/temp.jpg"
        await user.avatar_url.save(filename)
        file = discord.File(fp=filename)
        
        # Change profile picture from file
        fp = open(filename, 'rb')
        pfp = fp.read()
        await client.user.edit(avatar=pfp)
     

# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    
    # await ChangeUsernameAndAvatar(guildID=972274726456131594)
    # await ChangeUsernameAndAvatar(guildID=972274726456131594, user="Daniel")

    
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




