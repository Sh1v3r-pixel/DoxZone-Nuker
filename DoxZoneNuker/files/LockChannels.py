import discord
from discord.ext import commands
import asyncio

# Funzione per chiedere l'input all'utente
def chiedi_input():
    token = input("Inserisci il token del bot >>> ")
    server_id = int(input("Inserisci l'ID del server >>> "))
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
        print(f'Bot connesso come {bot.user}')
        guild = bot.get_guild(server_id)

        if guild is None:
            print("Server non trovato :(")
            await bot.close()
            return

        print(f"Inizio blocco canali nel server: {guild.name}")
        await lock_channels(bot, guild)
        print("Tutti i canali sono stati bloccati.")
        await bot.close()

    await bot.start(token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
