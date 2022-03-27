#import thư viện
from datetime import datetime
import pytz
from datetime import date
from discord.ext import commands
import requests
import os
#chỉnh prefix
prefix="?"

#khởi tạo bot
bot = commands.Bot(command_prefix = prefix)

#khai báo biến ngày tháng năm và dùng múi giờ việt nam
my_time =datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_date = date.today()

date_rn = my_date.strftime("%d")

month_rn = my_date.strftime("%m")

year_rn = my_date.strftime("%Y")

#event của bot
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
  
  
#command của bot
@bot.command()
async def khoidong(ctx):
  await ctx.send("Bot đã sẵn sàng!")
  
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
async def xemtt(ctx, arg1, arg2='', arg3=''):
  api_key = os.getenv('weather_api')
  
  link = 'http://api.weatherapi.com/v1/current.json?key='+api_key+'&q='+arg1+'%20'+arg2+'%20'+arg3+'&lang=vi'
  
  data = requests.get(link).json()
  
  city_temp =  round(data['current']['temp_c'])
  
  city_desc = data['current']['condition']['text']
  
  city = data['location']['name']
  
  last_update = data['current']['last_updated']
  
  wind_direction = data['current']['wind_dir']
  
  wind_speed = round(data['current']['wind_kph']/3.6)
  
  a = "Hiện tại thời tiết tại {0} được cập nhật gần nhất vào lúc {1} có nhiệt độ là {2} độ C; {3}\nHướng gió {4}, tốc độ gió {5}m/s ".format(city, last_update, city_temp, city_desc, wind_direction, wind_speed)
  
  await ctx.send(a)
  
@bot.command()
async def define(ctx, arg):
  words = arg
  
  api_address = "https://api.dictionaryapi.dev/api/v2/entries/en/"+words
  
  get_def = requests.get(api_address).json()
  
  word_def =  get_def[0]['word']
  
  word_def2 =  get_def[0]['meanings'][0]['definitions'][0]['definition']
  a = "Word: {0}\n Definition: {1}\n ".format(word_def, word_def2)
  await ctx.send(a)
    
#chạy bot
bot.run(os.getenv('secret_token'))
