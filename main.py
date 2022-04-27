#import thư viện
from datetime import datetime
import pytz
from datetime import date
from discord.ext import commands
import requests
import os
import discord
import time
import random


intents = discord.Intents.default()
intents.members = True
start_time = time.time()
#chỉnh prefix
prefix = ">"

#khởi tạo bot

bot = commands.Bot(command_prefix=prefix)
#khai báo biến ngày tháng năm và dùng múi giờ việt nam
my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_date = date.today()

date_rn = my_date.strftime("%d")

month_rn = my_date.strftime("%m")

year_rn = my_date.strftime("%Y")

a = ['Spirit', 'Curiosity', 'Opportunity']

b = random.choice(a)

send = None
#event của bot


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('Forecasting.'))
    print('We have logged in as {0.user}'.format(bot))
  
  


#command của bot
@bot.command()
async def khoidong(ctx):
    await ctx.send("Bot đã sẵn sàng!")


@bot.command()
async def dayrn(ctx):
    await ctx.send(date_rn)


@bot.command()
async def monthrn(ctx):
    await ctx.send(month_rn)


@bot.command()
async def yearrn(ctx):
    await ctx.send(year_rn)


#xem thời tiết
@bot.command()
async def xemtt(ctx, arg1, arg2='', arg3=''):
    api_key = os.getenv('weather_api')
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


    #xem định nghĩa của 1 từ nào đó
@bot.command()
async def define(ctx, arg4, arg5=''):
    words = arg4
    words2 = arg5

    api_address = "https://api.dictionaryapi.dev/api/v2/entries/en/" + words + words2

    get_def = requests.get(api_address).json()

    word_def = get_def[0]['word']

    word_def2 = get_def[0]['meanings'][0]['definitions'][0]['definition']
    a = "Word: {0}\n Definition: {1}\n ".format(word_def, word_def2)
    await ctx.send(a)


#xem giờ dùng epoch
@bot.command()
async def timern(ctx, ):

    timestamp = time.time()

    ts = datetime.fromtimestamp(timestamp + 25200).strftime('%H:%M:%S')

    await ctx.send(ts)


#xem ảnh
@bot.command()
async def apod(ctx, arg=date_rn, arg2=month_rn, arg3=year_rn):
    date = str(arg3) + '-' + str(arg2) + '-' + str(arg)
    apod_api = os.getenv('nasa_api')
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

    
      


@bot.command()
async def marspic(ctx, arg=b, arg2="", arg3=""):
    day = random.choice(range(0, 1001))
    arg3 = str(day)
    if arg2 != "":
        key = os.getenv('nasa_api')
        link = "https://api.nasa.gov/mars-photos/api/v1/rovers/" + arg + "/photos?sol=" + str(
            arg3) + "&api_key=" + key
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

    else:
        key = os.getenv('nasa_api')
        link = "https://api.nasa.gov/mars-photos/api/v1/rovers/" + arg + "/photos?sol=" + arg3 + "camera=" + arg2 + "&api_key=" + key
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


@bot.command()
async def hof(ctx):
  embed =  discord.Embed(title="Hall of fame", color = discord.Color.blue())
  embed.add_field(name="Hmm#3608", value="Thiết kế, làm bot.")
  embed.add_field(name="nolan ッ#6261", value="Thiết kế, quản lý cộng đồng.")
  embed.add_field(name="god staff jax#9036", value="Đưa ra ý tưởng, tài trợ.")
  embed.set_footer(text="Ngoài ra, chúng tôi còn cám ơn những người dùng bot, không có các bạn thì chúng tôi đã không có được như này. Mong các bạn sẽ có trải nghiệm tốt nhất khi dùng bot!")
  await ctx.send(embed=embed)

@bot.command()
async def sang(ctx):
  await ctx.send("Sang là cựu owner của \"Tên server nè\", là 1 trong những người đầu tiên đưa ra ý tưởng về bot. Không có sang, bot sẽ không có được như ngày hôm nay, mãi nhớ sang.")


print("The code ran in %s seconds" % (time.time() - start_time))


#chạy bot
bot.run(os.getenv('secret_token'))
