import os
import discord
from dotenv import load_dotenv
from discord.ext import commands



# get the environmental variable for the discord user
load_dotenv()  # load from the .en folder all thje environmental variables
BOTTOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create connection object
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')

# bot command to boop users
@bot.command(name='boop')
async def boop(ctx):
    await ctx.send('boop')

@bot.event
async def on_message(message):
    # prevent recursive call loop
    if message.author == bot.user:
        return
    
    lowerCase = message.content.lower()

    if 'cake' in lowerCase:
        await message.channel.send('the cake is a lie')


# @bot.event
# async def on_error(event):
#     if event == commands.errors.CommandNotFound:
#         pass


bot.run(BOTTOKEN)