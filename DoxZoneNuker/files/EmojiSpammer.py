import discord
import aiohttp
import asyncio
import sys
import time

def animazione_input(testo):
    for carattere in testo:
        sys.stdout.write("\033[38;2;255;0;0m" + carattere + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.02)

def chiedi_input(prompt):
    animazione_input(prompt)
    return input()

async def emoji_spammer(bot_token, server_id, emoji_url, emoji_name, quantity):
    intents = discord.Intents.default()
    intents.guilds = True
    intents.emojis = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Bot connesso come {client.user}")
        guild = client.get_guild(int(server_id))

        for i in range(quantity):
            await guild.create_custom_emoji(name=f"{emoji_name}_{i+1}", image=await fetch_image(emoji_url))
            print(f"Emoji '{emoji_name}_{i+1}' creata.")

        await client.close()

    async def fetch_image(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.read()

    await client.start(bot_token)

# Chiedere i dati all'utente con animazione per ogni input
bot_token = chiedi_input("Inserisci il token del bot >>> ")
server_id = chiedi_input("Inserisci l'ID del server >>> ")
emoji_url = chiedi_input("Inserisci il link dell'immagine per l'emoji >>> ")
emoji_name = chiedi_input("Inserisci il nome dell'emoji >>> ")
quantity = int(chiedi_input("Quante emoji vuoi creare >>> "))

# Esegui il loop di eventi
asyncio.run(emoji_spammer(bot_token, server_id, emoji_url, emoji_name, quantity))
