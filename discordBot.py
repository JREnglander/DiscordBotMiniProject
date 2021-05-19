import os
from dotenv import load_dotenv
from discord.ext import commands



# get the environmental variable for the discord user
load_dotenv()  # load from the .en folder all thje environmental variables
BOTTOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create connection object
bot = commands.Bot(command_prefix='!')

# bot command to boop users
@bot.command(name='boop')
async def boop(ctx):
    await ctx.send('boop')

bot.run(BOTTOKEN)