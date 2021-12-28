import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import random


class SpecialCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)

        server_name = str(ctx.guild.name)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description="",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Server Name", value=server_name, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Channels: ", value=len(
            ctx.message.guild.channels), inline=True)
        embed.add_field(name="Country", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name="Requested By: ", value=str(
            ctx.message.author.mention), inline=False)
        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def timenow(self, ctx):
        embed = discord.Embed(
            title="Time Now",
            description=f"See the footer to see the time for now!",
            timestamp=datetime.now(),
            color=0xd9bf18
        )
        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def nowtime(self, ctx):
        embed = discord.Embed(
            title="Time Now",
            description="See the footer to see the time for now!",
            timestamp=datetime.now(),
            color=0xd9bf18
        )
        await ctx.message.delete()

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def membercount(self, ctx):
        embed = discord.Embed(
            title="**Members**",
            description=f"{ctx.guild.member_count}",
            timestamp=datetime.now(),
            color=discord.Color.blue()
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)

    
    @commands.command(aliases=['announce'])
    @commands.has_permissions(manage_messages=True)
    async def announcement(self, ctx, *, announcement):
        await ctx.send(f"{announcement}")
        await ctx.message.delete()


    @commands.command(name="whois")
    @commands.has_permissions(manage_messages=True)
    async def whois(self, ctx, user: discord.Member = None):

        if user == None:
            user = ctx.author

        rlist = []
        for role in user.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)

        b = ", ".join(rlist)

        embed = discord.Embed(colour=user.color, timestamp=datetime.now())

        embed.set_author(name=f"User Info - {user}"),
        embed.set_thumbnail(url=user.avatar_url),

        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)

        embed.add_field(name='Created at:', value=user.created_at, inline=False)
        embed.add_field(name='Joined at:', value=user.joined_at, inline=False)

        embed.add_field(name='Bot?', value=user.bot, inline=False)

        embed.add_field(name=f'Roles:({len(rlist)})',
                        value=''.join([b]), inline=False)
        embed.add_field(name='Top Role:',
                        value=user.top_role.mention, inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(SpecialCommands(client))
