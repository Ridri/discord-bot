from bot_files.utils import *

#commande pour mettre un compteur sur le message de quelqu'un avant de le supprimer
async def compteur(ctx, compteur):
    await ctx.message.delete(delay = compteur)