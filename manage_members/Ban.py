from bot_files.utils import *

#commande pour ban quelqu'un
async def ban(ctx, member, reason):
    if member == ctx.message.author:
        await ctx.message.delete()
        await ctx.channel.send(f"{ctx.message.author.mention} Tu ne peux pas t'auto bannir !", delete_after = 5)
        return 
    if member == ctx.guild.owner:
        await ctx.message.delete()
        await ctx.channel.send(f"Le propriétaire du serveur ne peut pas être expulsé.", delete_after = 5)
        return
    await ctx.message.delete()
    try:
        await member.send(f"Vous avez été banni(e) de {ctx.guild} par {ctx.message.author.mention} pour la raison suivante : {reason}")
    except discord.errors.HTTPException:
        pass
    await member.ban(delete_message_days = 0, reason = reason)
    await ctx.channel.send(f"{member.mention} a été banni(e) de **{ctx.guild}** par {ctx.message.author.mention} pour la raison suivante : {reason}")