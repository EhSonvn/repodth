from discord.ext import commands
from datetime import date
from datetime import datetime
import pytz
import requests
import os

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

date_rn = my_time.strftime("%d")

month_rn = my_time.strftime("%m")

year_rn = my_time.strftime("%Y")

key = 'd6HuN4F1mCm4jRyKq2K2GqtHEyaa3jpCIyBrarW4'

class apod_cmd(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def apod(self, ctx, arg=date_rn, arg2=month_rn, arg3=year_rn):
    date = str(arg3) + '-' + str(arg2) + '-' + str(arg)
    apod_api = 'd6HuN4F1mCm4jRyKq2K2GqtHEyaa3jpCIyBrarW4'
    nasa_link = "https://api.nasa.gov/planetary/apod"
    param = {'api_key': apod_api, 'hd': True, 'date': date, 'thumbs': True}
    apod = requests.get(nasa_link, params=param)
    if apod.status_code == 404:
      await ctx.send("Hôm nay không có ảnh! Mã lỗi {0}".format(apod.status_code))
    else:
      data = apod.json()
      if data['media_type'] == 'image':
        await ctx.send(data['url'])
      else:
        yt_link = data['url']
        embed = yt_link.replace("embed/", "watch?v=")
        await ctx.send(embed)

def setup(bot):
  bot.add_cog(apod_cmd(bot))
    
  
  
