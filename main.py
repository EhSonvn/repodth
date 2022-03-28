#import thư viện
from datetime import datetime
import pytz
from datetime import date
from discord.ext import commands
import requests
import os
import discord
import time
import youtube_dl
from discord.utils import get
import time
#chỉnh prefix
prefix = "?"

#khởi tạo bot

bot = commands.Bot(command_prefix=prefix)



#khai báo biến ngày tháng năm và dùng múi giờ việt nam
my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).time()

my_date = date.today()

date_rn = my_date.strftime("%d")

month_rn = my_date.strftime("%m")

year_rn = my_date.strftime("%Y")



queue = []


#event của bot


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Forecasting.'))
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


@bot.command()
async def xemtt(ctx, arg1, arg2='', arg3=''):
    api_key = os.getenv('weather_api')

    link = 'http://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=' + arg1 + '%20' + arg2 + '%20' + arg3 + '&lang=en'

    data = requests.get(link).json()

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

    embed.add_field(name="Độ ẩm", value="{0}%".format(humidity), inline=True)

    embed.add_field(name="Hướng gió", value=wind_direction, inline=True)

    embed.add_field(name="Tốc độ gió",
                    value='{0}m/s'.format(wind_speed),
                    inline=True)

    await ctx.send(embed=embed)


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


@bot.command()
async def timern(ctx):

    timestamp = time.time()

    ts = datetime.fromtimestamp(timestamp + 25200).strftime('%H:%M:%S')

    await ctx.send(ts)
@bot.command(pass_context=True)
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_clients, guild=ctx.guild)
  if not ctx.message.author.voice:
    return await ctx.send("You're not in a voice channel!")
  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    await ctx.send(f"Join {channel}")
    voice = await channel.connect()
    print(f"Bot has joined {channel}")  
    
@bot.command(pass_context=True)
async def leave(ctx):
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_clients, guild=ctx.guild)  
  if voice and voice.is_connected():
    await voice.disconnect()
    await ctx.send(f"Left {channel}")
    print(f"The bot has left {channel}")
  else:
    print("Bot was told to leave in a channel that it didn't join")
    await ctx.send(f"Its seems like I haven't joined any channel, you mean join instead of leave?")

@bot.command()
async def ls(ctx, url):
  queue.append(str(url))
  await ctx.send("The song has been added into queue!")

@bot.command(pass_context=True)
async def play(ctx, url=""):  
  global voice2
  voice2 = ctx.voice_client 
  queue.append(str(url))  
  i = 0

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {
    'format':"bestaudio"
  }
  for i in range(len(queue)):
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(queue[i], download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      voice2.play(source)
      i += 1
      
  
  
      

 

@bot.command()
async def pause(ctx):
  await ctx.voice_client.pause()
  await ctx.send("Paused!")

@bot.command()
async def resume(ctx):
  await ctx.voice_client.resume()
  await ctx.send("Resumed!")


  
@bot.command()
async def showq(ctx):
  await ctx.send(queue)

@bot.command()
async def skip(ctx):
  await queue.pop(0)


#chạy bot
bot.run(os.getenv('secret_token'))
