import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("Missing DISCORD_TOKEN env var. See README_BOT.md")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user} (ID: {bot.user.id})")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Erreur: {error}")

if __name__ == "__main__":
    bot.run(TOKEN)
