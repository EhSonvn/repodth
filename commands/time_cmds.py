from discord.ext import commands
from datetime import datetime
import pytz
from datetime import date
import time

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_date = date.today()

date_rn = my_date.strftime("%d")

month_rn = my_date.strftime("%m")

year_rn = my_date.strftime("%Y")

class t_cmd(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hello(self, ctx):
    await ctx.send("Hello!")

  @commands.command()
  async def dayrn(self, ctx):
    await ctx.send(date_rn)
    
  @commands.command()
  async def monthrn(self, ctx):
    await ctx.send(month_rn)
    
  @commands.command()
  async def yearrn(self, ctx):
    await ctx.send(year_rn)

  @commands.command()
  async def timern(self, ctx):
    timestamp = time.time()
    ts = datetime.fromtimestamp(timestamp + 25200).strftime('%H:%M:%S')
    await ctx.send(ts)

def setup(bot):
  bot.add_cog(t_cmd(bot))