import discord
from discord.ext import commands


class ChatCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")


    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hi {ctx.author.mention}! How are you?")


    @commands.commands()
    async def hi(self, ctx):
        await ctx.reply(f"Hello {ctx.author.mention}! How are yu doing?")


    @commands.command()
    async def fine(self, ctx):
        pass


    @commands.command()
    async def bad(self, ctx):
        pass



def setup(client):
    client.add_cog(ChatCommands(client))
