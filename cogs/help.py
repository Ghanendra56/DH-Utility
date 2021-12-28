import discord
from discord.ext import commands
from datetime import datetime


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


        
    @commands.command()
    async def help(self, ctx):

        servericon = str(ctx.guild.icon_url)

        embed = discord.Embed(title="**Help Commands | DHS Official Bot**", description="Type D!help to get always help", timestamp=datetime.now(), color=discord.Color.random())
        embed.set_thumbnail(url=servericon)
        embed.add_field(name="**Command Prefix :- **",value="The command prefix of **DHS Official** bot is - d!",inline=False)

        embed.add_field(name="**Chat Commands (Chat With the Bot)**", value="ping\nhello\nhi\nfine\nbad\ninvite", inline=False)

        embed.add_field(name="Moderation Commands :- ", value="Kick\nBan\nUnban\nMute\nUnmute", inline=False)

        embed.add_field(name="Moderation Commands (Kick) :- ", value="Type - **d!kick**\nResult - The member will be **kicked** from the server\nNote :- \nThis command can be only used by the people who have **kick Members** permission roles in the server.", inline=True)

        embed.add_field(name="Moderation Commands (Ban) :- ", value="Type - **d!ban**\nResult - The member will be **Banned** from the server\nNote :- \nThis command can be only used by the people who have **ban Members** permission roles in the server.",inline=True)

        embed.add_field(name="Moderation Commands (Unban) :- ", value="Type - **d!unban**\nResult - The member will be **Unbanned** from the server\nNote :- \nThis command can be only used by the people who have **ban Members** permission roles in the server.", inline=True)

        embed.add_field(name="Moderation Commands (Mute) :- ",value="Type - **d!mute**\nResult - The member will be **Muted** from the server\nNote :- \nThis command can be only used by the people who have **Manage Messages** permission roles in the server.",inline=True)

        embed.add_field(name="Moderation Commands (Unmute) :- ",value="Type - **d!unmute**\nResult - The member will be **Unmuted** from the server\nNote :- \nThis command can be only used by the people who have **Manage Messages** permission roles in the server.", inline=True)
        
        embed.set_footer(text="This is the help commands for DHS | Official. \nNote - These commands can be changed in future!")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpCommand(client))
