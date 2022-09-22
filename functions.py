import discord
from unidecode import unidecode
from time import sleep
from client import client
from globalVar import *
import random
from os import listdir
from os.path import isfile, join
import datetime

async def ChangeUsernameAndAvatar(guildID, userID=None):
    guild = client.get_guild(guildID)
    myself  = discord.utils.get(guild.members, id=BOTanID)
    if userID == None:
        # Change back to BOTan
        
        await myself.edit(nick=None)
        
        filename = "images/BOTan_avatar.jpg"
        
        fp = open(filename, 'rb')
        pfp = fp.read()
        try:
            await client.user.edit(avatar=pfp)
        except discord.errors.HTTPException:
            print("I've changed avatar too fast")
        
    else:
        # Change username based on userID, and guildID
        user = discord.utils.get(guild.members, id=userID)
        
        await myself.edit(nick=user.display_name)
        
        # Save profile picture to file
        filename = "images/temp.jpg"
        await user.avatar.save(filename)
        file = discord.File(fp=filename)
        
        # Change profile picture from file
        fp = open(filename, 'rb')
        pfp = fp.read()
        try:
            await client.user.edit(avatar=pfp)
        except discord.errors.HTTPException:
            print("I've changed avatar too fast")
     
# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.invisible, activity=game)


# Draw random person that is not on voice channel
def DrawPerson(voiceChannel):
    availableUsers = users
    
    for member in voiceChannel.members:
        availableUsers = {key:val for key, val in availableUsers.items() if val != member.id}
       
    # print(availableUsers)
    
    if bool(availableUsers) == False:
        return None
    
    user = random.choice(list(availableUsers.keys()))
    return user
    
    
# draw sound based on drawed person
def DrawSound(user):
    path = "audio/{}/".format(user)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    sound = random.choice(onlyfiles)
    
    return("{}{}".format(path, sound))
    
isConnected = False
# Called when someone changes their voice state (connects to vc)
@client.event
async def on_voice_state_update(member, before, after):
    global isConnected
    # ignore ourself
    if member == client.user:
        return
    
    
    # If someone join channel (not change or deaf)
    if before.channel == None and after.channel != None:

        if isConnected:
            print("I'm already connected...")
            return
        
        # Get guild
        guild = after.channel.guild # Get guild

        now = datetime.datetime.now()
        print('-'*80)
        print("{}:".format(now))
        print("{} joined channel '{}' in '{}'".format(member, after.channel, guild))

        r = random.randint(1, 10) 
        # print("Selected number: {}".format(r))
        if r != 10:
            print("Decided not to join.")
            return
        
        print("Let's have some fun, joining...")

        isConnected = True 
        
        # change nick and avatar
        drawedUser = DrawPerson(voiceChannel=after.channel)
        if drawedUser == None:
            isConnected = False
            return
        print("I will imitate {}".format(drawedUser)) # debug
        
        await ChangeUsernameAndAvatar(guildID=guild.id, userID=users[drawedUser])
        sleep(5)
        
        # join
        await guild.change_voice_state(channel=after.channel) # Change voice state
        voiceConnection = await after.channel.connect() # connect
        
        # draw sentence
        sound = DrawSound(drawedUser)
        print("Playing {}...".format(sound)) # debug
        
        # play it
        source = discord.FFmpegPCMAudio(sound) # Get audio file
        voiceConnection.play(source) # play it
        
        # Wait until bot is playing
        while voiceConnection.is_playing():
            sleep(1)
        
        await voiceConnection.disconnect() # disconnect

        print("My job here is done, leaving...")
        # Change back to BOTan
        await ChangeUsernameAndAvatar(guildID=guild.id, userID=None)
        
        isConnected = False



