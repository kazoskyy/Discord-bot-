import discord
from discord.ext import commands
import datetime
import random
import asyncio
import os

bot = commands.Bot(command_prefix="-")
token = "discord bot token here"

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("i Don't know this command...")



async def chng_pr():
    await bot.wait_until_ready()

    statuses = ["-help", "Ruling over the Kingdom", "Having a fantastic day", "thinking about this server"]

    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(15)

path = 'Cogs'
for filename in os.listdir(path):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

@bot.command()
async def poll(ctx, *, question):
    msg = await ctx.send(question)
    reactions = ['👍', '👎']
    for emoji in reactions:
        await msg.add_reaction(emoji)

bot.loop.create_task(chng_pr())
bot.run(token)
