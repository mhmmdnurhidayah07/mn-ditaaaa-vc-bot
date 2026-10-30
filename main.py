import discord, asyncio, os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"MN Ditaaa hidup: {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("💖 MN udah join VC buat Ditaaa!")
    else:
        await ctx.send("Join VC dulu Jhon!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

@bot.event
async def on_voice_state_update(m, b, a):
    if m.id == bot.user.id and b.channel and not a.channel:
        await asyncio.sleep(2)
        try:
            await b.channel.connect()
        except:
            pass

bot.run(os.getenv("DISCORD_TOKEN"))
