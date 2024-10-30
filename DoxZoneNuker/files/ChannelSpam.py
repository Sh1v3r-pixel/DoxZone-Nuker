import discord
from discord.ext import commands
import asyncio
import random

def chiedi_input():
    token = input("Inserisci il token del bot >>> ")
    server_id = int(input("Inserisci l'ID del server >>> "))
    numero_canali = int(input("Quanti canali vuoi creare? >>> "))
    nome_canali_1 = input("Nome primo canale >>> ")
    nome_canali_2 = input("Nome secondo canale >>> ")
    nome_canali_3 = input("Nome terzo canale >>> ")
    
    return token, server_id, numero_canali, [nome_canali_1, nome_canali_2, nome_canali_3]

token, server_id, numero_canali, nomi_canali = chiedi_input()

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    guild = bot.get_guild(server_id)
    
    if guild is None:
        print("Server non trovato :(")
        await bot.close()
        return

    print("Creazione dei canali...")
 
    for _ in range(numero_canali):
        try:
            nome_canale = random.choice(nomi_canali)
            await guild.create_text_channel(nome_canale)
            print(f"Creato canale: {nome_canale}")
            await asyncio.sleep(0.2)
        except Exception as e:
            print(f"Errore nella creazione del canale: {e}")

    print("Tutti i canali creati.")
    await bot.close()

bot.run(token)
