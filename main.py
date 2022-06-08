from discord.ext import commands
import os
import discord
import time

start_time = time.time()
 
prefix = ">"

bot = commands.Bot(command_prefix=prefix)

for file in os.listdir("commands"):
    if file.endswith(".py"):
        bot.load_extension(f'commands.{file[:-3]}')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('Happy Pride Month!'))
    print('We have logged in as {0.user}'.format(bot))  
   

print("The code ran in %s seconds" % (time.time() - start_time))


bot.run(os.getenv('secret_token'))
