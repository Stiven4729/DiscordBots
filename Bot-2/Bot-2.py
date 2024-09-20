import discord
from discord.ext import commands
from googletrans import Translator
from Conexion import token
#from textblob import TextBlob

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Is ready for answer...")

@bot.command()
async def en(ctx, *, word):
    try:
        text = Translator()
        translation1 = text.translate(word, dest='en').text
        await ctx.send(f"el texto traducido a ingles es >>> {translation1}")
    except Exception as err:
        print(err)


@bot.command()
async def es(ctx, *, word):
    try:
        text = Translator()
        translation1 = text.translate(word, dest='es').text
        await ctx.send(f"el texto traducido a español es >>> {translation1}")
    except Exception as err:
        print(err)

bot.run(f'{token}')
