import discord

client = discord.client()

@client.event
async def on_message(message):
    print(message.content)

#le bot répond à une "commande" mais ce n'est pas le test de ping
@client.event
async def on_message1(message):
    if message.content == "Ping":
        await message.channel.send('Pong !')



"""
@client.event
async def on_message(message):
    print(message.content)
"""

"""
@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send('Pong !')
"""