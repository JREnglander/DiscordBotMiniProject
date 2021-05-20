import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import weatherRequester


# get the environmental variable for the discord user
load_dotenv()  # load from the .en folder all thje environmental variables
BOTTOKEN = os.getenv('DISCORD_TOKEN')

# create connection object
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')

@bot.command(name='weather', help='gets the weather for a given location')
async def weather(ctx,city ,state='',country=''):
    wr = weatherRequester.weatherRequester()
    print(city)
    currWeather = wr.requestWeather(city,state,country)
    weatherResponse = f'Currently, its {currWeather[0]} degrees outside with {currWeather[1]}% humidity and {currWeather[2]}'
    await ctx.send(weatherResponse)


# TODO: Figure out how to access and make HTTP requests to Weather.com API (Will probably put in a separate class)
# TODO: Figure out how to use tasks to make timely alerts
# TODO: Make commands to get weather for certain place

# run the bot
bot.run(BOTTOKEN)
