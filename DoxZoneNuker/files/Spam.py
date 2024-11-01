import discord
from discord.ext import commands
import asyncio
import time
import sys

# Funzione per l'animazione della scrittura in rosso
def animazione_testo(testo):
    for carattere in testo:
        sys.stdout.write("\033[38;2;255;0;0m" + carattere + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

def chiedi_input():
    animazione_testo("Inserisci il token del bot >>> ")
    token = input("\033[38;2;255;0;0m")  # Colore per input
    animazione_testo("Inserisci l'ID del server >>> ")
    server_id = int(input("\033[38;2;255;0;0m"))
    animazione_testo("Inserisci l'ID del canale in cui vuoi spammare >>> ")
    channel_id = int(input("\033[38;2;255;0;0m"))
    animazione_testo("Cosa vuoi spammare? >>> ")
    messaggio_spam = input("\033[38;2;255;0;0m")
    animazione_testo("Quanti messaggi vuoi spammare? >>> ")
    numero_messaggi = int(input("\033[38;2;255;0;0m"))
    
    return token, server_id, channel_id, messaggio_spam, numero_messaggi

token, server_id, channel_id, messaggio_spam, numero_messaggi = chiedi_input()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    animazione_testo(f'Bot connesso come {bot.user}')
    guild = bot.get_guild(server_id)
    
    if guild is None:
        animazione_testo("Server non trovato :(")
        await bot.close()
        return

    channel = bot.get_channel(channel_id)
    
    if channel is None:
        animazione_testo("Canale non trovato :(")
        await bot.close()
        return

    animazione_testo(f"Inizio spam nel canale: {channel.name}")

    for _ in range(numero_messaggi):
        try:
            await channel.send(messaggio_spam)
            animazione_testo(f"Spammato in {channel.name}: {messaggio_spam}")
            await asyncio.sleep(0.01)
        except Exception as e:
            animazione_testo(f"Errore nel spammare nel canale {channel.name}: {e}")
            break

    animazione_testo("Spam completato :)")

bot.run(token)
