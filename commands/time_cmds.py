from discord.ext import commands
import time
from datetime import datetime
import pytz


class TCmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def dayrn(self, ctx):
        await ctx.send(datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%d"))

    @commands.command()
    async def monthrn(self, ctx):
        await ctx.send(datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%m"))

    @commands.command()
    async def yearrn(self, ctx):
        await ctx.send(datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%Y"))

    @commands.command()
    async def timern(self, ctx):
        await ctx.send(datetime.fromtimestamp(time.time() + 25200).strftime('%H:%M:%S'))


def setup(bot):
    bot.add_cog(TCmd(bot))
