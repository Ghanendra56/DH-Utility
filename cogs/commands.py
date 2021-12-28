import discord
from discord import embeds
from discord.ext import commands
from datetime import datetime


class ChatCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ping(self, ctx):
        ping_msg = await ctx.send(f"Pong! ``{round(self.client.latency*1000)} ms``")
        await ctx.message.delete()
        await ping_msg.add_reaction("🏓")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def vote(self, ctx):
        embed = discord.Embed(
        title = "**Vote for Our Server**",
        description = "<:ophunt:890466902764318730> Make Sure To Vote Our Server Every 12hrs, to get special role <@&902427106284306462> On Your  Profile!!\n<:ophunt:890466902764318730> Vote Link :- https://top.gg/servers/887267018808655903/vote",
        color = discord.Color.blue()
        )
        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pong(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Ping ``{round(self.client.latency*1000)}ms``")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def hello(self, ctx):
        hello_msg = await ctx.send(f"Hi! {ctx.author.mention} How are you?")
        await ctx.message.delete()
        await hello_msg.add_reaction("👐")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def hi(self, ctx):
        hi_msg = await ctx.send(f"Hello! {ctx.author.mention} How are you?")
        await ctx.message.delete()
        await hi_msg.add_reaction("👐")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def fine(self, ctx):
        await ctx.send("Wow! Good.")
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slap(self, ctx, member: discord.Member, *, reason=None):
        await ctx.reply(f"You slapped {member.mention}, for - {reason}")
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def bad(self, ctx):
        await ctx.send("Oh, noo!")
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def inv(self, ctx):
        embed = discord.Embed(
            title="**Dude Hunter** Server Invite Link",
            description="Server Invite Link - https://discord.gg/xAR5QzXngm",
            color=discord.Color.blue(),
        )
        await ctx.message.delete()

        await ctx.send(embed=embed)

    @commands.command()
    async def ytlinko(self, ctx):

        await ctx.message.delete()

        await ctx.send("**Dude Hunter YT Link** - https://www.youtube.com/channel/UCmqa434jsHDOJPlczAllppw")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def prefixes(ctx):
        embed = discord.Embed(
            title="**Prefixes**",
            description="Prefixes - d!, D!",
            color=ctx.author.color
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(ChatCommands(client))
