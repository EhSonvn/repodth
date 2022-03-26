#import thư viện
from datetime import datetime
import pytz
from datetime import date
from discord.ext import commands
import requests
#chỉnh prefix
prefix="?"

#dùng api của openweather để lấy thông tin thời tiết
api_request ='http://api.openweathermap.org/data/2.5/weather?q=dalat&appid=cee343d33e41970dd63c44b39c8620ab'
data = requests.get(api_request).json()
format_data = data['main']

a = "Nhiệt độ của thành phố Đà Lạt hôm nay có nhiệt độ thấp nhất là {0}, nhiệt độ cao nhất là {1} Độ C".format(
int(format_data['temp_min']-273),int(format_data['temp_max']-273))


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
    if message.content.startswith("goodnight"):
        await message.channel.send("Goodnight")

  

  
  
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
@bot.command()
async def nhietdodl(ctx):
  await ctx.send(a)

   
 
#chạy bot
bot.run("OTU3MTUzNjM2MDYzMDEwODM3.Yj6oyQ.9Pf7DRtwihdpSVj-iErozsOZDVs")
