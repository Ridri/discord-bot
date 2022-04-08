from bot_files.utils import *
from bot_files.var import *

#commande pour changer le statut et/ou l'activité du bot
async def status(ctx, status, activity, type):
    try: 
        await ctx.message.delete() 
    except: 
        pass
    if ctx.author.id == owner_id:
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
        print(f"Statut modifié : \n status = \"{status}\" \n activity = \"{activity}\"")
    else:
        await ctx.channel.send(f"Seul le propriétaire du bot peut utiliser cette commande.", delete_after = 5)