import discord
from discord.ext import commands


class FilteredWords(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        pass

def setup(client):
    client.add_cog(FilteredWords(client))