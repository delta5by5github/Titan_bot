import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def anime(ctx):
    # Replace this with the code to fetch and send an anime picture
    await ctx.send("Here's an anime picture!")

@bot.command()
async def titan(ctx, action):
    if action == 'slap':
        # Replace this with the code to send a slap gif
        await ctx.send("Titan slapping gif")
    elif action == 'hug':
        # Replace this with the code to send a hug gif
        await ctx.send("Titan hugging gif")
    else:
        await ctx.send("Invalid action. Available actions: slap, hug")

bot.run('YOUR_BOT_TOKEN')
