import discord
from discord.ext import commands
import asyncio
import sys
import time

# Funzione per l'animazione della scrittura in rosso
def animazione_testo(testo):
    for carattere in testo:
        sys.stdout.write("\033[38;2;255;0;0m" + carattere + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

# Funzione per chiedere l'input all'utente
def chiedi_input():
    animazione_testo("Inserisci il token del bot >>> ")
    token = input("\033[38;2;255;0;0m")  # Colore per input
    animazione_testo("Inserisci l'ID del server >>> ")
    server_id = int(input("\033[38;2;255;0;0m"))
    return token, server_id

# Funzione principale per bloccare i canali
async def lock_channels(bot, guild):
    for channel in guild.channels:
        try:
            if isinstance(channel, discord.TextChannel):
                await channel.set_permissions(guild.default_role, send_messages=False)
                print(f"Canale {channel.name} bloccato.")
            elif isinstance(channel, discord.VoiceChannel):
                await channel.set_permissions(guild.default_role, connect=False)
                print(f"Canale vocale {channel.name} bloccato.")
            await asyncio.sleep(0.5)  # Ritardo tra le operazioni
        except Exception as e:
            print(f"Errore nel bloccare il canale {channel.name}: {e}")

async def main():
    token, server_id = chiedi_input()
    
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        animazione_testo(f'Bot connesso come {bot.user}')
        guild = bot.get_guild(server_id)

        if guild is None:
            print("Server non trovato :(")
            await bot.close()
            return

        animazione_testo(f"Inizio blocco canali nel server: {guild.name}")
        await lock_channels(bot, guild)
        animazione_testo("Tutti i canali sono stati bloccati.")
        await bot.close()

    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
