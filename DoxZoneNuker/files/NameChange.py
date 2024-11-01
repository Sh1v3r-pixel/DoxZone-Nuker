import discord
from discord.ext import commands
import os
import time
import sys
import asyncio

# Funzione per l'animazione della scrittura in rosso
def animazione_testo(testo):
    for carattere in testo:
        sys.stdout.write("\033[38;2;255;0;0m" + carattere + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

# Funzione principale per cambiare il nome
async def change_names(bot_token, server_id, new_name):
    intents = discord.Intents.default()
    intents.members = True  # Assicurati di avere accesso ai membri
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        animazione_testo(f'Bot connesso come {bot.user}')
        guild = bot.get_guild(int(server_id))
        
        if guild is None:
            animazione_testo("ID del server non valido.")
            await bot.close()
            return

        # Cambia il nome di ogni membro
        for member in guild.members:
            try:
                await member.edit(nick=new_name)
                animazione_testo(f'Cambiato il nome di {member.name} in {new_name}')
            except Exception as e:
                animazione_testo(f'Errore nel cambiare il nome di {member.name}: {e}')

        animazione_testo("Cambio dei nomi completato.")
        await bot.close()

    await bot.start(bot_token)

if __name__ == "__main__":
    animazione_testo("Inserisci il token del bot >>> ")
    bot_token = input("\033[38;2;255;0;0m")  # Rimuove colore dopo input
    animazione_testo("Inserisci l'ID del server >>> ")
    server_id = input("\033[38;2;255;0;0m")
    animazione_testo("Inserisci il nuovo nome per i membri >>> ")
    new_name = input("\033[38;2;255;0;0m")

    # Avvia la funzione per cambiare i nomi
    asyncio.run(change_names(bot_token, server_id, new_name))
