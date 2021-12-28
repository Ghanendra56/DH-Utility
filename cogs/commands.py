import discord
from discord import embeds
from discord.ext import commands
from datetime import datetime


class ChatCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")


    @commands.command()
    async def slap(self, ctx, member: discord.Member, *, reason="No Reason was given for **Slapping**"):
        
        embed = discord.Embed(title="Slapped!!!", description=f"**{ctx.author}** Slapped {member.mention}  ||  Reason: **{reason}**", timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def wish(self, ctx, member: discord.Member, *, wish="No Reason was given for **Wishing**"):
        
        embed = discord.Embed(title="Wish!", description=f"**{ctx.author}** Wished - **{wish}** to {member.mention}", timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def greet(self, ctx, member: discord.Member, *, greet_msg="No **Greet Message** was given!"):

        embed = discord.Embed(title="Greeted!", description=f"**{ctx.author}** Greeted - **{greet_msg}** to {member.mention}", timestamp=datetime.utcnow(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hi {ctx.author.mention}! How are you?")


    @commands.command()
    async def hi(self, ctx):
        await ctx.reply(f"Hello {ctx.author.mention}! How are yu doing?")


    @commands.command(aliases=['good'])
    async def fine(self, ctx):
        await ctx.reply("Pretty Good!")


    @commands.command()
    async def bad(self, ctx):
        pass


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def inv(self, ctx):

        embed = discord.Embed(title="**Dude Hunter** Server Invite Link", description="Server Invite Link - https://discord.gg/xAR5QzXngm", color=discord.Color.blue())

        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command()
    async def github(self, ctx):

        embed = discord.Embed(title="Github __DH Utility__", description="__DH Utility__  Github Repository  -  https://github.com/ArinjoyProgrammer/DH-Utility", timestamp=datetime.utcnow(), color=discord.Color.purple())

        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command()
    async def ytlinko(self, ctx):
        await ctx.message.delete()
        
        await ctx.send("**Dude Hunter YT Link** - https://www.youtube.com/channel/UCmqa434jsHDOJPlczAllppw")


    @commands.command()
    async def prefixes(self, ctx):

        embed = discord.Embed(title="**Prefixes**", description="Prefixes - ``d!``, ``D!``", color=ctx.author.color)
        
        await ctx.message.delete()
        
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(ChatCommands(client))
