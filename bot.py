import discord

from TOKEN import TOKEN

from client import client
from functions import *
from globalVar import *


# Do przetestowania:

# Wykrywanie, że ktoś dołączył na kanał głosowy [DONE]
# Pobieranie nicku osoby + avataru(?), którą bot będzie imitować
# Spróbować zmienić nick i avatar bota
# Dołączenie na kanał głosowy [DONE]
# Puszczenie mp3 [DONE]


# Program:

# Wykrycie, że ktoś dołączył
# Losowanie czy też dołączyć
# Jeśli tak to pobrać nick
# Wylosować dźwięk odpowiedni dla danej osoby
# Zagrać dźwięk
# Wyjść


client.run(TOKEN)
