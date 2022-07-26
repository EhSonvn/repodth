from discord.ext import commands
import os
import discord
 
prefix = ">"

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

for file in os.listdir("commands"):
    if file.endswith(".py"):
        bot.load_extension(f'commands.{file[:-3]}')
print("All cogs are loaded")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print('We have logged in as {0.user}'.format(bot))  


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("An error happened: Missing Required Argument.")

@bot.command()
async def test(ctx):
    await ctx.send("Bot is running!")  
    
    
bot.run(os.getenv('bot_token'))
