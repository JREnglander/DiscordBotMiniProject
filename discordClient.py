# creating a connection to Discord
import os
import discord
from dotenv import load_dotenv

# get the environmental variable for the discord user
load_dotenv() # load from the .en folder all thje environmental variables
BOTTOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create connection object
client = discord.Client()

# this fuction runs when the bot has connected to discord
@client.event
async def on_ready():
    # Old way to ensure that you get a specific guild
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # new way use discord utility functions
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    
    # OR another option is to simply get the guild that matches the environmental variable
    # guild = discord.utils.get(client.guilds, name=GUILD)


    # print(f'{client.user} has connected to the following Guilds:\n'
    # f'{guild.name}(id: {guild.id})\n'
    # )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')
    print(f'{client.user.name} has joined to Discord')

# function for giving a message to a new member of a guild
@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord Server')

@client.event
async def on_message(message):
    # if the message was made by the bot do not do anything
    # prevent loop of bot messages
    if message.author == client.user:
        return
    
    # make case insensitive:
    nonCaseSensitive = message.content.lower()
    response = ''

    if nonCaseSensitive == 'boop':
        response = 'boop'
    elif 'cake' in nonCaseSensitive:
        response = 'The Cake is a lie'
    elif message.content == 'raise_exception':
        raise discord.DiscordException
    
    await message.channel.send(response)


@client.eventasync def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':






# this runs the bot
client.run(BOTTOKEN)
