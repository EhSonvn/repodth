from discord.ext import commands
import os
import discord
import time

start_time = time.time()
 
prefix = ">"

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

for file in os.listdir("commands"):
    if file.endswith(".py"):
        bot.load_extension(f'commands.{file[:-3]}')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print('We have logged in as {0.user}'.format(bot))  
   

print("The code ran in %s seconds" % (time.time() - start_time))


bot.run(os.getenv('OTU3MTUzNjM2MDYzMDEwODM3.GSzE00.wQ4ZToaTaV9PNMj0fLeIfvInWVYuGamGxNu9uA'))
