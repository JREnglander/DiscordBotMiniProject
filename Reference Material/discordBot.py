import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random


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
@bot.command(name='boop', help='boops you')
async def boop(ctx):
    await ctx.send('boop')

# this command has converters in the params to make sure the parameters are the proper type
@bot.command(name='roll_dice', help='rolls an given number of given sided dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1,number_of_sides+1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.event
async def on_message(message):
    # prevent bot from responding to itself
    if message.author == bot.user:
        return

    # if the message is a bot command (starts with a !) then process the command rather than checking if cake is in the name
    # this also allows for more easter eggs because 
    if message.content[0] == '!':
        await bot.process_commands(message)
    elif 'cake' in message.content:
        await message.channel.send('the cake is a lie!')
    elif 'boop' in message.content:
        await message.channel.send('boop')
    
    

bot.run(BOTTOKEN)
