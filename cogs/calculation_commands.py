from types import ClassMethodDescriptorType
import discord
from discord.ext import commands
from datetime import datetime


class CalculationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def add(self, ctx, num1: int, num2: int):

        embed = discord.Embed(title="Addition", description=num1+num2, timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def sub(self, ctx, num1: int, num2: int):

        embed = discord.Embed(title="Substraction", description=num1-num2, timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def mul(self, ctx, num1: int, num2: int):

        embed = discord.Embed(title="Multiplication", description=num1*num2, timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def div(self, ctx, num1: int, num2: int):

        embed = discord.Embed(title="Division", description=num1/num2, timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(CalculationCommands(client))
