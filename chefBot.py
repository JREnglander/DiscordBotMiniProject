import os
from dotenv import load_dotenv
from discord.ext import commands

# get the bot token
load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

chefBot = commands.Bot(command_prefix=".")

# notification in console that bot connected to discord
@chefBot.event
async def on_ready():
    print(f'{chefBot.user.name} is connected to Discord')

# 