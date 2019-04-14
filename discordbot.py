import discord
from discord.ext import commands

client = commands.Bot(command_prefix=";")

token = "NTYyMDM2MjUwOTQxNDU2Mzg0.XLNItQ.0iGZo-CsEDrYQ9w3NUMASDPD8S4"

@client.event
async def on_ready():
    print('This script is ready to be used!')
    print('This script was created by ChasingNachos.')
    print('We have successfully logged in as...')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    print('Running script...')
    print('Script is running. You are ready to go!')

@client.event
async def on_message(message):
    user = message.author
    content = message.content
    print(f"{user} said [{content}]")

    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(token)
