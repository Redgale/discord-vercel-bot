import os
import discord
import requests
from discord.ext import commands

DISCORD_TOKEN = os.environ["MTM3NDE5MzQ1NzY0MzM5MzE3NQ.GiTnyy.8CwFKJq5oO78o8oGkSTw1AcfEQS0jT12KGMjDo"]
DEPLOY_HOOK_URL = os.environ["https://api.vercel.com/v1/integrations/deploy/prj_APq54Cyskvi2heTlu0qlVoaeZoKm/YObrmhFsgm"]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def deploy(ctx):
    await ctx.send("🚀 Deploying via Vercel API...")

    response = requests.post(DEPLOY_HOOK_URL)

    if response.status_code == 200:
        await ctx.send("✅ Deployment triggered! Check your Vercel dashboard.")
    else:
        await ctx.send("❌ Failed to trigger deployment.")
        print(response.text)

bot.run(DISCORD_TOKEN)
