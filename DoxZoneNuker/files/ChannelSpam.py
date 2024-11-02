import time
import discord
from discord.ext import commands

red_color = "\033[38;2;255;0;0m"
reset_color = "\033[0m"

def animazione_scrittura(messaggio):
    for char in messaggio:
        print(red_color + char + reset_color, end='', flush=True)
        time.sleep(0.03)  # velocita anim

def chiedi_input():
    animazione_scrittura("Token bot >>> ")
    token = input()
    
    animazione_scrittura("Server ID >>> ")
    server_id = int(input())
    
    return token, server_id

async def lock_channels(guild):
    for channel in guild.channels:
        try:
            if isinstance(channel, discord.TextChannel):
                await channel.set_permissions(guild.default_role, send_messages=False)
                print(f"Canale {channel.name} bloccato.")
            elif isinstance(channel, discord.VoiceChannel):
                await channel.set_permissions(guild.default_role, connect=False)
                print(f"Canale vocale {channel.name} bloccato.")
            await asyncio.sleep(0.5)
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
        await lock_channels(guild)
        print("Tutti i canali sono stati bloccati.")
        await bot.close()

    await bot.start(token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
