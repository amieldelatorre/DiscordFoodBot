import os
import discord
import requests 
import json 

from service import Service
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

# load environment variables 
TOKEN = os.getenv("DISCORD_TOKEN")

# set up bot client 
bot = commands.Bot(command_prefix='foodBot!')

# events 
@bot.event
async def on_ready():
    print(
        f"FoodBot has connected to Discord!\n"
    )

# commands
@bot.command(name='food', help="Retrieves a random meal.")
async def food(context):
    result = Service.get_random_food()
    print(f"Summoned from {context.guild}")
    await context.send(f"You are eating {result['name']}")
    await context.send(result['image'])

@bot.command(name='drink', help="Retrieves a random alcoholic drink.")
async def food(context):
    result = Service.get_random_drink()
    print(f"Summoned from {context.guild}")
    await context.send(f"You are drinking {result['name']}")
    await context.send(result['image'])




bot.run(TOKEN)