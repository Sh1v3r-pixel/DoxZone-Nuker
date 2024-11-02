import discord
from discord.ext import commands
import sys

if len(sys.argv) < 3:
    print("Uso: python KickAll.py <bot_token> <server_id>")
    sys.exit(1)

bot_token = sys.argv[1]
server_id = sys.argv[2].strip()

if not server_id.isdigit():
    print("L'ID del server deve essere un numero valido.")
    sys.exit(1)

server_id = int(server_id)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")
    guild = bot.get_guild(server_id)

    if guild is None:
        print("ID del server non valido. Verifica l'ID e riprova.")
        await bot.close()
        return

    print(f"Inizio a cacciare membri dal server: {guild.name}")

    for member in guild.members:
        if member.id != bot.user.id:
            try:
                await member.kick(reason="Cacciato dal bot")
                print(f"Cacciato: {member.name}#{member.discriminator}")
            except discord.Forbidden:
                print(f"Impossibile cacciare {member.name}#{member.discriminator}: permessi insufficienti.")
            except discord.HTTPException as e:
                print(f"Impossibile cacciare {member.name}#{member.discriminator}: errore di rete - {e}")
            except Exception as e:
                print(f"Errore imprevisto durante il kick di {member.name}#{member.discriminator}: {e}")

    print("Operazione di kick completata.")
    await bot.close()

bot.run(bot_token)
