#import des bibliothèques 
import discord
from discord.ext import commands
import os

#définition des instances
default_intents = discord.Intents.all()
client = commands.Bot(command_prefix = "$", intents = default_intents)

#activation des intents relatifs aux membres
default_intents.members = True