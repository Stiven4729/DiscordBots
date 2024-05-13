import discord
from discord.ext import commands
from googletrans import Translator
#from textblob import TextBlob

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Is ready for answer...")

@bot.command()
async def traducir(ctx, *, word):
    try:
        channel = ctx.channel.name
        text = Translator()
        translation1 = text.translate(word, dest='en').text
        await ctx.send(f"canal {channel} el texto traducido a español es {translation1}")
    except Exception as err:
        print(err)

bot.run("{Key_Bot}")