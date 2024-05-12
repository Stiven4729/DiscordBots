import discord
from discord.ext import commands
from googletrans import Translator
#from textblob import TextBlob

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Is ready for answer...")

@bot.command()
async def Mensseger(ctx, *, word):
    try:
        channel = ctx.channel.name
        text = Translator()
        translation = text.translate(word, dest='es').text
        await ctx.send(f"canal {channel} el texto traducido a español es {translation}")
    except Exception as err:
        print(err)

bot.run("{Key_Bot}")
