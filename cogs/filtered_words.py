import discord
from discord.ext import commands


class FilteredWords(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        filtered_words = ['fuck', 'foolish']
        msg = message.content

        for items in filtered_words:
            if msg.startswith(items):
                await message.channel.send(":x: These types of messages aren't allowed in this server!\n***Message Deleted***")
                await message.delete()

            elif msg.endswith(items):
                await message.channel.send(":x: These types of messages aren't allowed in this server!\n***Message Deleted***")
                await message.delete()

            elif msg(items):
                await message.channel.send(":x: These types of messages aren't allowed in this server!\n***Message Deleted***")
                await message.delete()

def setup(client):
    client.add_cog(FilteredWords(client))
