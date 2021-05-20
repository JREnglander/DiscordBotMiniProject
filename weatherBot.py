import os
from dotenv import load_dotenv
from discord.ext import commands, tasks


# get the environmental variable for the discord user
load_dotenv()  # load from the .en folder all thje environmental variables
BOTTOKEN = os.getenv('DISCORD_TOKEN')

# create connection object
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')

# TODO: Figure out how to access and make HTTP requests to Weather.com API (Will probably put in a separate class)
# TODO: Figure out how to use tasks to make timely alerts
# TODO: Make commands to get weather for certain place

# run the bot
bot.run(BOTTOKEN)