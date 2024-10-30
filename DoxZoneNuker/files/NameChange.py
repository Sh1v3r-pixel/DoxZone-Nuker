import discord
from discord.ext import commands
import os

# Funzione principale per cambiare il nome
async def change_names(bot_token, server_id, new_name):
    intents = discord.Intents.default()
    intents.members = True  # Assicurati di avere accesso ai membri
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Bot connesso come {bot.user}')
        guild = bot.get_guild(int(server_id))
        if guild is None:
            print("ID del server non valido.")
            await bot.close()
            return

        # Cambia il nome di ogni membro
        for member in guild.members:
            try:
                await member.edit(nick=new_name)
                print(f'Cambiato il nome di {member.name} in {new_name}')
            except Exception as e:
                print(f'Errore nel cambiare il nome di {member.name}: {e}')

        await bot.close()

    await bot.start(bot_token)

if __name__ == "__main__":
    bot_token = input("Inserisci il token del bot >>> ")
    server_id = input("Inserisci l'ID del server >>> ")
    new_name = input("Inserisci il nuovo nome per i membri >>> ")

    # Avvia la funzione per cambiare i nomi
    import asyncio
    asyncio.run(change_names(bot_token, server_id, new_name))
