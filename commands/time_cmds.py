from discord.ext import commands
from time_vars import time_var


class t_cmd(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hello(self, ctx):
    await ctx.send("Hello!")

  @commands.command()
  async def dayrn(self, ctx):
    await ctx.send(time_var.date_rn)
    
  @commands.command()
  async def monthrn(self, ctx):
    await ctx.send(time_var.month_rn)
    
  @commands.command()
  async def yearrn(self, ctx):
    await ctx.send(time_var.year_rn)

  @commands.command()
  async def timern(self, ctx):
    await ctx.send(time_var.ts)

def setup(bot):
  bot.add_cog(t_cmd(bot))
