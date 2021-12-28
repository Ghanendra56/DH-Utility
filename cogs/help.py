import discord
from discord.ext import commands
from datetime import datetime


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        
        embed = discord.Embed(title="Help Command  ||  **DH Utility**", description="The Help Commands is not ready yet!\nThis Help Command will be ready soon!", timestamp=datetime.utcnow(), color=discord.Color.random())

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpCommand(client))
