from discord.ext import commands
import discord
import random
import os
import requests
import os

a = ['Spirit', 'Curiosity', 'Opportunity']

b = random.choice(a)


class MarsPic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mars_pic(self, ctx, arg=b, arg2="", arg3=""):
        day = random.choice(range(0, 1001))
        arg3 = str(day)
        if arg2 != "":
            link = "https://api.nasa.gov/mars-photos/api/v1/rovers/" + arg + "/photos?sol=" + str(
                arg3) + "&api_key=" + os.getenv('nasa_api_key')
            api = requests.get(link)
            if api.status_code == 200:
                data = api.json()
                d = []
                for i in data['photos']:
                    d.append(i['img_src'])
                c = random.choice(d)
                embed = discord.Embed(
                    title='Ảnh chụp bề mặt sao hoả từ {0}'.format(arg),
                    colour=discord.Color.blue())
                embed.set_image(url=c)
                embed.set_footer(text="Link ảnh: {0}".format(c))
                await ctx.send(embed=embed)
            elif api.status_code == 500:
                await ctx.send(
                    "Lỗi server, mời bạn thử lại lần sau! Mã lỗi: {0}".format(
                        api.status_code))
            elif api.status_code == 400 or api.status_code == 404:
                await ctx.send(
                    "Đã có lỗi khi nhập thông tin! Bạn đã gõ đúng chính tả chưa? Mã lỗi: {0}"
                    .format(api.status_code))
            elif api.status_code == 403:
                await ctx.send(
                    "Truy cập bị cấm, xin hãy thử lại lần sau! Mã lỗi: {0}".format(
                        api.status_code))

        else:
            link = "https://api.nasa.gov/mars-photos/api/v1/rovers/" + arg + "/photos?sol=" + arg3 + "camera=" + arg2 + "&api_key=" + os.getenv(
                'nasa_api_key')
            api = requests.get(link)
            if api.status_code == 200:
                data = api.json()
                a = []
                for i in data['photos']:
                    a.append(i['img_src'])
                b = random.choice(a)
                embed = discord.Embed(
                    title='Ảnh chụp bề mặt sao hoả từ {0}'.format(arg),
                    colour=discord.Color.blue())
                embed.set_image(url=b)
                embed.set_footer(text="Link ảnh: {0}".format(b))
                await ctx.send(embed=embed)
            elif api.status_code == 500:
                await ctx.send(
                    "Lỗi server, mời bạn thử lại lần sau! Mã lỗi: {0}".format(
                        api.status_code))
            elif api.status_code == 400 or api.status_code == 404:
                await ctx.send(
                    "Đã có lỗi khi nhập thông tin! Bạn đã gõ đúng chính tả chưa? Mã lỗi: {0}"
                    .format(api.status_code))
            elif api.status_code == 403:
                await ctx.send(
                    "Truy cập bị cấm, xin hãy thử lại lần sau! Mã lỗi: {0}".format(
                        api.status_code))


def setup(bot):
    bot.add_cog(MarsPic(bot))
