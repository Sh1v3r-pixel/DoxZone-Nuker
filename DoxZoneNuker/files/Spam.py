import discord
from discord.ext import commands
import asyncio

def chiedi_input():
    token = input("Inserisci il token del bot >>> ")
    server_id = int(input("Inserisci l'ID del server >>> "))
    channel_id = int(input("Inserisci l'ID del canale in cui vuoi spammare >>> "))
    messaggio_spam = input("Cosa vuoi spammare? >>> ")
    numero_messaggi = int(input("Quanti messaggi vuoi spammare? >>> "))  # Parentesi chiusa aggiunta qui
    
    return token, server_id, channel_id, messaggio_spam, numero_messaggi

token, server_id, channel_id, messaggio_spam, numero_messaggi = chiedi_input()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    guild = bot.get_guild(server_id)
    
    if guild is None:
        print("Server non trovato :(")
        await bot.close()
        return

    channel = bot.get_channel(channel_id)
    
    if channel is None:
        print("Canale non trovato :(")
        await bot.close()
        return

    print(f"Inizio spam nel canale: {channel.name}")

    for _ in range(numero_messaggi):
        try:
            await channel.send(messaggio_spam)
            print(f"Spammato in {channel.name}: {messaggio_spam}")
            await asyncio.sleep(0.01)  # Intervallo ridotto a 0.05 secondi
        except Exception as e:
            print(f"Errore nel spammare nel canale {channel.name}: {e}")
            break

    print("Spam completato :)")

bot.run(token)
