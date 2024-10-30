import discord
import aiohttp
import asyncio

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
            # Creazione dell'emoji
            await guild.create_custom_emoji(name=f"{emoji_name}_{i+1}", image=await fetch_image(emoji_url))
            print(f"Emoji '{emoji_name}_{i+1}' creata.")

        # Chiudi il client
        await client.close()

    async def fetch_image(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.read()

    await client.start(bot_token)

# Chiedere i dati all'utente
bot_token = input("Inserisci il token del bot >>> ")
server_id = input("Inserisci l'ID del server >>>")
emoji_url = input("Inserisci il link dell'immagine per l'emoji >>> ")
emoji_name = input("Inserisci il nome dell'emoji >>> ")
quantity = int(input("Quante emoji vuoi creare >>> "))  # Richiesta del numero di emoji da creare

# Esegui il loop di eventi
asyncio.run(emoji_spammer(bot_token, server_id, emoji_url, emoji_name, quantity))
