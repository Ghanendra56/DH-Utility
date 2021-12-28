import discord
from discord.ext import commands
from datetime import datetime


class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        embed = discord.Embed(
        title = "",
        description = f"<:Yalgaar:897805835630170143> {member.mention} was banned",
        color = discord.Color.green()
        )
        await ctx.send(embed=embed)
        embed = discord.Embed(
        title = "",
        description = f"<:Yalgaar:897805835630170143> {member.mention}You are Banned from the Server  |  reason - {reason}",
        color = discord.Color.green()
        )
        await ctx.message.delete()
        await member.send(embed=embed)

    #The below code unbans player.
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
        await ctx.message.delete()
            
    # kicked
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(
        embed = discord.Embed(
            description = f"User {member} has been kicked",
            timestamp = datetime.now(),
            color = 0x5de622
        )
        )
        await member.send(f"You have been kicked from {member.guild.name} | reason: {reason}")
        await ctx.message.delete()


    # mute
    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(
        description=f"<:Yalgaar:897805835630170143> {member.mention} was muted ", colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"<:Yalgaar:897805835630170143  You have been muted from: {guild.name} reason: {reason}")
        await ctx.message.delete()

    # Timed Mute

    # unmute


    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f" you have unmutedd from: - {ctx.guild.name}")
        embed = discord.Embed(
            title="unmute", description=f" unmuted-{member.mention}", colour=discord.Colour.light_gray())
        await ctx.message.delete()
        await ctx.send(embed=embed)

    # Warn


    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        embed = discord.Embed(
            description=f"**<:Yalgaar:897805835630170143> {member.mention} has been warned.**",
            timestamp=datetime.now(),
            color=discord.Color.red()
        )

        await member.send(
        embed = discord.Embed(
            description = f"<:Yalgaar:897805835630170143> You were warned in Dude Hunter Server for: {reason}"
        )
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=3):
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(ModerationCommands(client))
