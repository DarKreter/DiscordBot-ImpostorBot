import discord
from TOKEN import TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# from functions import *
# from globalVar import *


client.run(TOKEN)