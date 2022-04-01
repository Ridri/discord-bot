from bot_files.utils import *

#commande ping
async def ping(ctx):
	await ctx.channel.send(f"Pong  🏓  ! {round(client.latency * 1000)}ms")