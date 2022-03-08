#import des bibliothèques 
import discord
import os
import keep_alive
from discord.ext import commands

#définition des instances
default_intents = discord.Intents.default()
client = commands.bot(command_prefix="$", intents = default_intents)

#activation des intents relatifs aux membres
default_intents.members = True

#indique que le bot est prêt à recevoir des instructions (/commandes)
@client.event
async def on_ready():
    print("The bot is ready !")

#message d'accueil (s'affiche sur replit et sur discord)
@client.event
async def on_member_join(member):
    join_channel = client.get_channel("mettre l'ID du salon en question")
    join_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

#commande de suppression de messages
async def on_message(message):
    if message.content.startwith("!del"):
        number = int(message.content.split()[1])
        messages_history = await message.channel.history(limit = number + 1).flatten()
        for each_message in messages_history:
            await each_message.delete()

#commande pour supprimer des messages
@client.command(name = "del")
async def delete(ctx, number: int):
    messages_history = await ctx.channel.history(limit = number + 1).flatten
    for each_message in messages_history:
        await each_message.delete()

#import de keep_alive pour que replit n'arrête pas l'execution du repl
keep_alive.keep_alive()

#connexion/mise en ligne du client + utilisation du token avec os pour le sécuriser
client.run(os.environ["TOKEN"])