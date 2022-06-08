from discord.ext import commands
import discord

class random_cmds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def code(self, ctx):
    embed = discord.Embed(title="Source code", colour=discord.Color.blue())
    embed.add_field(name="Link github", value="https://github.com/EhSonvn/repodth")
    embed.set_footer(text="Muốn đóng góp cùng chúng tôi, hãy liên lệ Hmm#3608!")
    await ctx.send(embed=embed)

  @commands.command()
  async def hoanglinh(self, ctx):
    await ctx.send("anh quận béo có thương iem hong??")

  @commands.command()
  async def khoidong(self, ctx):
    await ctx.send("Bot đã sẵn sàng!")

    
def setup(bot):
  bot.add_cog(random_cmds(bot))