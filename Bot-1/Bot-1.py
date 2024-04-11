import discord
from discord.ext import commands
import youtube_dl
from Conexion import token


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

names = []

@bot.event
async def on_ready():
    print(f"I am {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

bot.run(f'{token}')
