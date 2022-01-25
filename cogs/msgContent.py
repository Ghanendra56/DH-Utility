import discord
from discord.ext import commands


class msgContent(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("dude") and message.content.endswith("dude"):
            await message.channel.send("Dude Op!!!!!! <:ophunt:890466902764318730>")



def setup(client):
    client.add_cog(msgContent(client))
