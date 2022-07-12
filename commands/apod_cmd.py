from discord.ext import commands
from time_vars import time_var
import requests
import os 



class apod_cmd(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def apod(self, ctx, arg=time_var.date_rn, arg2=time_var.month_rn, arg3=time_var.year_rn):
    date = str(arg3) + '-' + str(arg2) + '-' + str(arg)
    apod_api = 'd6HuN4F1mCm4jRyKq2K2GqtHEyaa3jpCIyBrarW4'
    nasa_link = "https://api.nasa.gov/planetary/apod"
    param = {'api_key': os.getenv('nasa_api_key'), 'hd': True, 'date': date, 'thumbs': True}
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
    
  
  
