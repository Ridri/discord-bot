from bot_files.utils import *

#commande pour kick (expulser) quelqu'un
async def kick(ctx, member, reason):
    if member == ctx.message.author:
        await ctx.message.delete()
        await ctx.channel.send(f"{ctx.message.author.mention} Tu ne peux pas t'auto expulser !", delete_after = 5)
        return 
    if member == {ctx.guild.owner}:
        await ctx.message.delete()
        await ctx.channel.send(f"Le propriétaire du serveur ne peut pas être expulsé.", delete_after = 5)
        return
    await ctx.message.delete()
    try:
        await member.send(f"Vous avez été expulsé(e) de {ctx.guild} par {ctx.message.author.mention} pour la raison suivante : {reason}")
    except discord.errors.HTTPException:
        pass
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member.mention} a été expulsé de **{ctx.guild}** par {ctx.message.author.mention} pour la raison suivante : {reason}")