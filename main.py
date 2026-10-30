import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")
VOICE_CHANNEL_ID = 123456789012345678

@bot.event
async def on_ready():
    print(f"MN ❤️ Ditaaa Bot Hidup! {bot.user}")
    for guild in bot.guilds:
        channel = guild.get_channel(VOICE_CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                await channel.connect()
                print(f"Udah join VC: {channel.name}")
            except:
                pass

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == bot.user.id and before.channel and not after.channel:
        await asyncio.sleep(2)
        channel = before.channel.guild.get_channel(before.channel.id)
        try:
            await channel.connect()
        except:
            pass

bot.run(TOKEN)
