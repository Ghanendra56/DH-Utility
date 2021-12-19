import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random

load_dotenv()

prefixes = 'd!', 'D!', '.'

client = commands.Bot(command_prefix = prefixes)

# Removed Commands
client.remove_command("help")


@client.event
async def on_ready():
    print(f"{client.user} is Online on Discord!")

async def ch_pr():
    await client.wait_until_ready()

    statuses = ['d!help', 'discord.gg/xAR5QzXngm']

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=status))
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(5)

client.loop.create_task(ch_pr())



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(os.getenv('token'))
