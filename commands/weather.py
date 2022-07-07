import discord
from discord.ext import commands
import requests 
import os

api_key = os.getenv('9cd9b907b5ee44cf86c41145222703')

class weather(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def xemtt(self, ctx, arg1, arg2='', arg3=''):
    link = 'http://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=' + arg1 + '%20' + arg2 + '%20' + arg3 + '&lang=en'
    api = requests.get(link)
    data = api.json()
    if api.status_code == 200:
        city_temp = round(data['current']['temp_c'], 2)
        city_desc = data['current']['condition']['text']
        city = data['location']['name']
        last_update = data['current']['last_updated']
        wind_direction = data['current']['wind_dir']
        country = data['location']['country']
        humidity = data['current']['humidity']
        wind_speed = round(data['current']['wind_kph'] / 3.6, 2)
        embed = discord.Embed(
            title='Thông tin về thời tiết tại {0} thuộc {1}'.format(
                city, country),
            description='Dữ liệu mới nhật được cập nhật vào lúc {0}'.
            format(last_update),
            colour=discord.Color.blue())
        embed.add_field(name="Nhiệt độ",
                        value="{0} độ C".format(city_temp),
                        inline=True)
        embed.set_footer(text='Dữ liệu từ weatherapi.')
        embed.add_field(name='Tình hình', value=city_desc, inline=True)
        embed.add_field(name="Độ ẩm",
                        value="{0}%".format(humidity),
                        inline=True)
        embed.add_field(name="Hướng gió", value=wind_direction, inline=True)
        embed.add_field(name="Tốc độ gió",
                        value='{0}m/s'.format(wind_speed),
                        inline=True)
        await ctx.send(embed=embed)
    elif api.status_code == 500:
        await ctx.send(
            "Lỗi server, mời bạn thử lại lần sau! Mã lỗi: {0}".format(
                api.status_code))
    elif api.status_code == 400 or api.status_code == 404:
        await ctx.send(
            "Thành phố không tồn tại! Bạn đã gõ đúng chính tả chưa? Mã lỗi: {0}"
            .format(api.status_code))
    elif api.status_code == 403:
        await ctx.send(
            "Truy cập bị cấm, xin hãy thử lại lần sau! Mã lỗi: {0}".format(
                api.status_code))

def setup(bot):
  bot.add_cog(weather(bot))
  
