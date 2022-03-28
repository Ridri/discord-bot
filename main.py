#import des bibliothèques 
import discord
import os
import keep_alive
from discord.ext import commands

#définition des instances
default_intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents = default_intents)

#activation des intents relatifs aux membres
default_intents.members = True

#indique que le bot est prêt à recevoir des instructions (commandes)
@client.event
async def on_ready():
    print("The bot is ready !")

"""
J'ai perdu beaucoup de temps (environ 3j) à essayer de créer une variable pour contenir le id_channel puis le mettre dans le on_member_join (au lieu de mettre directement l'id du salon)
"""

#message d'accueil
@client.event
async def on_member_join(member):
    await client.get_channel(878673900194660442).send(f"Bienvenue sur **{member.guild}** {member.mention} !")

#message de "leaving"
@client.event
async def on_member_remove(member):
    await client.get_channel(878673900194660442).send(f"{member.mention} a quitté le serveur.")
    
#commande pour changer le statut et/ou l'activité du bot
@client.command(name = "status", aliases = ["act", "activity"], help = "Modifie l'activité et/ou le statut du bot. $fusion [statut (online, idle, offline, dnd)] [activité] [type (G, L, W, P)]")
async def change(ctx, status: discord.Status, activity: str, type: str):
    try: 
        await ctx.message.delete() 
    except: 
        pass
    if ctx.author.id == 691985543126581280:
        if type == "Game" or type == "G":
            type = 1
        elif type == "Listen" or type == "L":
            type = 2
        elif type == "Watch" or type == "W":
            type = 3
        elif type == "Participate" or type == "P":
            type = 5
        else:
            return
        await client.change_presence(status = status, activity = discord.Activity(type = type, name = activity))
    else:
        await ctx.channel.send(f"Seul le propriétaire du bot peut utiliser cette commande.", delete_after = 5)

#commande ping
@client.command(name = "ping", help = "Renvoie la latence (temps de réponse) du bot. $ping")
async def ping(ctx):
	await ctx.send(f"Pong  🏓  ! {round(client.latency * 1000)}ms")

#commande pour mettre un compteur sur le message de quelqu'un avant de le supprimer
@client.command(name = "compteur", aliases = ["cpt"], help = "Met un compteur sur le message de quelqu'un et le supprime à la fin du compteur. $compteur [nombre entier] [le message que tu veux]", ignore_extra = True)
async def compteur(ctx, compteur: int):
    await ctx.message.delete(delay = compteur)

#commande pour supprimer des messages
@client.command(name = "del", aliases = ["suppr", "clear"], help = "Commande pour supprimer des messages. $suppr [nombre entier]")
@commands.has_permissions(manage_messages = True)
async def delete(ctx, number: int):
    if number >= 0:
        await ctx.channel.purge(limit=number + 1)
    else:
        await ctx.message.delete()
        await ctx.channel.send(f"Erreur ! \"{number}\" n'est pas une option valide !", delete_after = 5)
        return

#commande pour kick (expulser) quelqu'un
@client.command(name = "kick", help = "Commande pour expulser quelqu'un du serveur. $kick [Membre] [Raison (optionnel)]")
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, reason: str = None):
    if member == ctx.message.author:
        await ctx.message.delete()
        await ctx.channel.send(f"{ctx.message.author.mention} Tu ne peux pas t'auto expulser !", delete_after = 5)
        return 
    if member == {ctx.guild.owner}:
        await ctx.message.delete()
        await ctx.channel.send(f"On ne peut pas tuer Dieu !", delete_after = 5)
        return
    await ctx.message.delete()
    try:
        await member.send(f"Vous avez été expulsé(e) de {ctx.guild} par {ctx.message.author.mention} pour la raison suivante : {reason}")
    except discord.errors.HTTPException:
        pass
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member.mention} a été expulsé de **{ctx.guild}** par {ctx.message.author.mention} pour la raison suivante : {reason}")

#commande pour ban quelqu'un
@client.command(name = "ban", help = "Commande pour ban quelqu'un. $ban [Membre] [Raison (optionnel)]")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, reason: str = None):
    if member == ctx.message.author:
        await ctx.message.delete()
        await ctx.channel.send(f"{ctx.message.author.mention} Tu ne peux pas t'auto bannir !", delete_after = 5)
        return 
    if member == ctx.guild.owner:
        await ctx.message.delete()
        await ctx.channel.send(f"On ne peut pas tuer Dieu !", delete_after = 5)
        return
    await ctx.message.delete()
    try:
        await member.send(f"Vous avez été banni(e) de {ctx.guild} par {ctx.message.author.mention} pour la raison suivante : {reason}")
    except discord.errors.HTTPException:
        pass
    await member.ban(delete_message_days = 0, reason = reason)
    await ctx.channel.send(f"{member.mention} a été banni(e) de **{ctx.guild}** par {ctx.message.author.mention} pour la raison suivante : {reason}")

#import de keep_alive pour que replit n'arrête pas l'execution du repl
keep_alive.keep_alive()

#connexion/mise en ligne du client + utilisation du token avec os pour le sécuriser
client.run(os.environ["TOKEN"])