from discord.ext import commands
import json
import discord

class up_down(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def upf(self, ctx, arg, *stuff):
    msg  = ctx.message
    if str(msg.attachments) == "[]":
      await ctx.send("You didnt send any files!")
    else:
      split_v1 = str(msg.attachments).split("filename='")[1]
      filename = str(split_v1).split("' ")[0]
      await msg.attachments[0].save(fp="./uploaded_files/{}".format(filename))
      info = {
        filename: arg
        }
      json_object = json.dumps(info)
      with open("info.json", "a") as f:
        f.write("{} \n".format(json_object))
        await ctx.send("File uploaded.")
        await ctx.send("You file id is {}!".format(arg))

  @commands.command()
  async def getf(self, ctx, arg):
    json_data = [json.loads(line) for line in open('info.json','r')]
    for file_name in json_data:
      for i in file_name:
        if file_name[i] == arg:
          b = file_name.keys()
    for i in b:
      a = "./uploaded_files/{}".format(i)
      await ctx.send(file=discord.File(a))
      await ctx.send("File sent!")   

def setup(bot):
  bot.add_cog(up_down(bot))