#"""
#import des fichiers et bibliothèques nécessaires
from bot_files.utils import *
from cmd_files.Files import *
from bot_files.var import *

#indique que le bot est prêt à recevoir des instructions (commandes)
@client.event
async def on_ready():
    print("The bot is ready !")

#message d'accueil
@client.event
async def on_member_join(member):
    await client.get_channel(878673900194660442).send(f"Bienvenue sur **{member.guild}** {member.mention} !")

#message de "leaving"
@client.event
async def on_member_remove(member):
    await client.get_channel(878673900194660442).send(f"{member.mention} a quitté le serveur.")
    
#commande pour changer le statut et/ou l'activité du bot
@client.command(name = "status", aliases = ["act", "activity"], help = "Modifie l'activité et/ou le statut du bot. $change [statut (online, idle, offline, dnd)] [activité] [type (G, L, W, P)]")
async def status(ctx, status: discord.Status, activity: str, type: str):
    await Status.status(ctx, status, activity, type)

#commande ping
@client.command(name = "ping", help = "Renvoie la latence (temps de réponse) du bot. $ping")
async def ping(ctx):
	await Ping.ping(ctx)

#commande pour mettre un compteur sur le message de quelqu'un avant de le supprimer
@client.command(name = "compteur", aliases = ["cpt"], help = "Met un compteur sur le message de quelqu'un et le supprime à la fin du compteur. $compteur [nombre entier] [le message que tu veux]", ignore_extra = True)
async def compteur(ctx, compteur: int):
    await Compteur.compteur(ctx, compteur)

#commande pour supprimer des messages
@client.command(name = "del", aliases = ["suppr", "clear", "clean", "purge"], help = "Commande pour supprimer des messages. $suppr [nombre entier]")
@commands.has_permissions(manage_messages = True)
async def delete(ctx, number: int):
    await Delete.delete(ctx, number)

#commande pour kick (expulser) quelqu'un
@client.command(name = "kick", help = "Commande pour expulser quelqu'un du serveur. $kick [Membre] [Raison (optionnel)]")
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, reason: str = None):
    await Kick.kick(ctx, member, reason)

#commande pour ban quelqu'un
@client.command(name = "ban", help = "Commande pour ban quelqu'un. $ban [Membre] [Raison (optionnel)]")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, reason: str = None):
    await Ban.ban(ctx, member, reason)

@client.command(name = "close")
async def close_connexion(ctx, confirm: bool = False):
    await Close.close(ctx, confirm)

#import de keep_alive pour que replit n'arrête pas l'execution du repl
keep_alive.keep_alive()

#connexion/mise en ligne du client + utilisation du token avec os pour le sécuriser
client.run(os.environ["TOKEN"])
#"""