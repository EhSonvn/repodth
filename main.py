#import thư viện
from datetime import datetime
import pytz
from datetime import date
from discord.ext import commands

#chỉnh prefix
prefix="?"

#chỉnh format của ngày tháng năm
date_format = "%y/%m/%d"

#khởi tạo bot
bot = commands.Bot(command_prefix = prefix)

#khai báo biến ngày tháng năm và dùng múi giờ việt nam
my_time =datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()
my_date = date.today()
date_rn = my_date.strftime("%d")
month_rn = my_date.strftime("%m")
year_rn = my_date.strftime("%Y")

#event của bot
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
  
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hi")
    await bot.process_commands(message)
  
#command của bot
@bot.command()
async def dayrn(ctx):
  await ctx.send(date_rn)
@bot.command()
async def timern(ctx):
  await ctx.send(my_time)
@bot.command()
async def monthrn(ctx):
  await ctx.send(month_rn)
@bot.command()
async def yearrn(ctx):
  await ctx.send(year_rn)
 
#chạy bot
bot.run(token)
