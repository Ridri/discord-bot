from bot_files.utils import *
from bot_files.var import *
from cmd_files.files import *

async def close_connexion(ctx, confirm):
    if ctx.author.id == owner_id:
        if confirm == True:
            await Status.status(ctx, offline, "", W)
            await ctx.send("Fermeture du client")
            await client.close()
        else:
            return
    else:
        ctx.send("Commande réservée au propriétaire du bot.", delete_after = 5)