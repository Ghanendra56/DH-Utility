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
    async def hack(self, ctx, member : discord.Member):

        random_password = ['36b29c', 'kt764a', '45cvv76', 'fh90;ll', 'gda889', 'kla789', 'kkk89q', 'ff89f52', '95632lrt']

        await ctx.send(f"Hacking Satrted on {member}")
        await ctx.send(f"Hacking Username and Password of {member}")
        await asyncio.sleep(4)
        await ctx.send(f"Hacked!\nUsername - ``{member}\nPassword - **{random.choice(random_password)}**")
        await asyncio.sleep(4)
        await ctx.send("Hacking Completed 20%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 30%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 50%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Epic Games and Steam Account")
        await asyncio.sleep(2)
        await ctx.send("Hacking Epic Games and Steam Account Completed Successfully")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 80%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 90%")
        await asyncio.sleep(4)
        await ctx.send(f"A **Dangerous Hacking** Completed on **{member}**\nDon't mind this was a really **Fake Hack**")



def setup(client):
    client.add_cog(SpecialCommands(client))