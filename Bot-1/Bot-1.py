import discord
from discord.ext import commands
import youtube_dl
from Conexion import token
import subprocess

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"I am {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command()
async def calcular(ctx, expresion):
    try:
        resultado = eval(expresion)
        await ctx.send(f"El resultado de la expresión '{expresion}' es: {resultado}")
    except Exception as e:
        await ctx.send(f"Ha ocurrido un error al calcular la expresión: {e}")

@bot.command()
async def ejecutar_comando(ctx, *, comando):
    try:
        # Ejecutar el comando de manera segura utilizando subprocess
        proceso = subprocess.Popen(comando.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()

        # Truncar la salida y el error si exceden el límite de caracteres
        salida_truncada = salida[:1990].decode(errors='ignore') + '...' if len(salida) > 1990 else salida.decode(errors='ignore')
        error_truncado = error[:1990].decode(errors='ignore') + '...' if len(error) > 1990 else error.decode(errors='ignore')

        # Enviar la salida del comando al canal de Discord
        await ctx.send(f"**Salida:**```{salida_truncada}```\n**Error:**```{error_truncado}```")
    except Exception as e:
        await ctx.send(f"Error al ejecutar el comando: {e}")

bot.run(f'{token}')
