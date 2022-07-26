from discord.ext import commands
import requests
import os
from datetime import datetime
import pytz


class ApodCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def apod(self, ctx, arg=datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%d"),
                   arg2=datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%m"),
                   arg3=datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%Y")):
        date = str(arg3) + '-' + str(arg2) + '-' + str(arg)
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
    bot.add_cog(ApodCmd(bot))
