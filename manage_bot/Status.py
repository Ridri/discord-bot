from bot_files.utils import *

#commande pour changer le statut et/ou l'activité du bot
async def change(ctx, status, activity, type):
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