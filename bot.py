import discord

from TOKEN import TOKEN

from client import client
from functions import *
from globalVar import *


# Do przetestowania:

# Wykrywanie, że ktoś dołączył na kanał głosowy [DONE]
# Pobieranie nicku osoby + avataru(?), którą bot będzie imitować [DONE]
# Spróbować zmienić nick i avatar bota [DONE]
# Dołączenie na kanał głosowy [DONE]
# Puszczenie mp3 [DONE]


# Program:

# Wykrycie, że ktoś dołączył [DONE]
# Losowanie czy też dołączyć 
# Jeśli tak to pobrać nick [DONE]
# Wylosować dźwięk odpowiedni dla danej osoby
# Zagrać dźwięk [DONE]
# Wyjść [DONE]


client.run(TOKEN)
