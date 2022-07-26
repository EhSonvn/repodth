import discord
from discord.ext import commands
import requests


class WordDef(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, arg4, arg5=''):
        words = arg4
        words2 = arg5
        api_address = "https://api.dictionaryapi.dev/api/v2/entries/en/" + words + words2
        get_def = requests.get(api_address).json()
        word_def1 = get_def[0]['word']
        word_def2 = get_def[0]['meanings'][0]['definitions'][0]['definition']
        a = "Word: {0}\n Definition: {1}\n ".format(word_def1, word_def2)
        await ctx.send(a)


def setup(bot):
    bot.add_cog(WordDef(bot))
