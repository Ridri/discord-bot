#commande pour unban quelqu'un
@client.command(name = "unban", help = "Commande pour unban quelqu'un. $unban [membre]")
@commands.has_permissions(ban_members = True)
async def unban(ctx, member):
    await ctx.message.delete()
    #
    banned_members = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for banned_user in banned_members:
        user = banned_user.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
    #
    await ctx.channel.send(f"{member.mention} a été unban de **{ctx.guild}** par {ctx.message.author.mention}.")
    try:
        await member.send(f"Vous avez été unban de **{ctx.guild}** par {ctx.message.author.mention}.")
    except discord.errors.HTPException:
        pass