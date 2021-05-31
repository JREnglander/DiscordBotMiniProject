import os
from dotenv import load_dotenv
from discord.ext import commands
from foodRequester import foodRequester

# get the bot token
load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

chefBot = commands.Bot(command_prefix=".")

# notification in console that bot connected to discord
@chefBot.event
async def on_ready():
    print(f'{chefBot.user.name} is connected to Discord')

@chefBot.command(name = 'food')
async def food(ctx, query: str, start=0, end=10):
        fr = foodRequester()
        if fr.currentRecipe == None:
            fr.requestEdamam(query, start, end)
        else:
            food = fr.currentRecipe
            response = f"Here try {food['name']}\n Here's where its from: {food['source']}"
            await ctx.send(response)
            
            
chefBot.run(botToken)