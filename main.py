import os
import discord
from discord.ext import commands
from rolls import roll_dice
from dotenv import load_dotenv

load_dotenv()
TOKEN_DS = os.getenv('TOKEN_DS')

intents = discord.Intents.all()
bot = commands.Bot(";", intents = intents)

@bot.event
async def on_ready():
    comandos = await bot.tree.sync()
    print(f"{len(comandos)} comandos reconhecidos")
    print("Inicializado")

@bot.tree.command()
async def roll(interact: discord.Interaction, quantidade: int, lados: int, vantagem: int = 0):
    resposta = roll_dice(quantidade, lados, vantagem)
    await interact.response.send_message(resposta)

@bot.tree.command()
async def secret_roll(interact: discord.Interaction, quantidade: int, lados: int, vantagem: int = 0):
    resposta = roll_dice(quantidade, lados, vantagem)
    await interact.response.send_message(resposta, ephemeral=True)

bot.run(TOKEN_DS)