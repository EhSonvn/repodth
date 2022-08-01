from sys import api_version
import discord
from discord.ext import commands
import requests
import os


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def xemtt(self, ctx, arg1, arg2='', arg3=''):
        link = 'http://api.weatherapi.com/v1/current.json?key=' + os.getenv(
            'weather_api_key') + '&q=' + arg1 + '%20' + arg2 + '%20' + arg3 + '&lang=en'
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

    @commands.command()
    async def dubao(self, ctx, day, arg1, arg2='', arg3=''):
        link = "https://api.weatherapi.com/v1/forecast.json?key={0}&q=" + arg1 + '%20' + arg2 + '%20' + arg3 +"&days={1}&aqi=no&alerts=no".format(os.getenv('weather_api_key'), day)
        api = requests.get(link)
        data = api.json()
        if api.status_code == 200:
            city = data['location']['name']
            country = data['location']['country']
            last_update = data['current']['last_updated']
            embed1 = discord.Embed(title="Thông tin dự báo thời tiết tại {0} thuộc {1}", description="Được cấp nhật lần cuối vào lúc {2}").format(city, country, last_update)
            
            for i in range(0, day+1):
                embed = discord.Embed(title="Vào ngày {1}").format(data['forecast']['forecastday'][i]['day'])
                embed.add_field(name="Nhiệt độ thấp nhất: {0}\n Nhiệt độ cao nhất: {1}").format(data['forecast']['forecastday'][i]['day']['mintemp_c'], data['forecast']['forecastday'][i]['day']['maxtemp_c'])
                embed.add_filed(name="Tốc độ gió cao nhất: {1}").format(round(data['forecast']['forecastday'][i]['day']['maxwind_kph']/3.6))
                embed.add_field(name="Độ ẩm trung bình: {1}").format(data['forecast']['forecastday'][i]['day']['avghumidity'])
                await ctx.send(embed)
            
            await ctx.send(embed1)
        
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
    bot.add_cog(Weather(bot))
