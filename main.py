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
async def xemtt(ctx, arg):
  user_api = os.getenv('weather_api')
  a = arg
  api_add = "https://api.openweathermap.org/data/2.5/weather?q="+a+"&appid="+user_api+"&lang=vi"
  
  api_data = requests.get(api_add).json()
  
  temp_city = ((api_data['main']['temp']) - 273.15)
  
  weather_desc = api_data['weather'][0]['description']
  
  hmdt = api_data['main']['humidity']
  
  wind_spd = api_data['wind']['speed']
  
  city_name =  api_data['name']
  
  report = "Tình hình thời tiết tại {0}: {1}\n Nhiệt độ: {2}\n Tốc độ gió: {3}m/s\n Độ ẩm: {4}%".format(city_name, weather_desc, temp_city, wind_spd, hmdt)
  await ctx.send(report)
  
@bot.command()
async def define(ctx, arg):
  words = arg
  
  api_address = "https://api.dictionaryapi.dev/api/v2/entries/en/"+words
  
  get_def = requests.get(api_address).json()
  
  word_def =  get_def[0]['word']
  
  word_def2 =  get_def[0]['meanings'][0]['definitions'][0]['definition']
  a = "Word: {0}\n Definition: {1}\n".format(word_def, word_def2)
  await ctx.send(a)
    

#chạy bot
bot.run(os.getenv('secret_token'))
