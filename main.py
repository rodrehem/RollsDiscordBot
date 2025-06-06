import os
import discord
from discord.ext import commands
from rolls import roll_requisition, coin_flip
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
async def roll(interact: discord.Interaction, dados: str):
    resposta = roll_requisition(dados)
    await interact.response.send_message(resposta)

@bot.tree.command()
async def secret_roll(interact: discord.Interaction, dados: str):
    resposta = roll_requisition(dados)
    await interact.response.send_message(resposta, ephemeral=True)

@bot.tree.command()
async def coin(interact: discord.Interaction):
    resposta = coin_flip()
    await interact.response.send_message(resposta)

@bot.tree.command()
async def secret_coin(interact: discord.Interaction):
    resposta = coin_flip()
    await interact.response.send_message(resposta, ephemeral=True)

bot.run(TOKEN_DS)

