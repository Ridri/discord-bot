from bot_files.utils import *

#commande pour supprimer des messages
async def delete(ctx, number):
    if number >= 0:
        await ctx.channel.purge(limit=number + 1)
    else:
        await ctx.message.delete()
        await ctx.channel.send(f"Erreur ! \"{number}\" n'est pas une option valide !", delete_after = 5)
        return