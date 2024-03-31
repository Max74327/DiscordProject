import discord
from discord.ext import commands
import random
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)


class Character:
    pass


@bot.command(name='roll')
async def my_randint(ctx, data):
    output = list()
    for _ in range(int(data[:data.index('d')])):
        output.append(str(random.randint(1, int(data[data.index('d') + 1:]) + 1)))
    await ctx.send(f'{sum(output)}\n{" ".join(output)}')


@bot.command(name='d20')
async def d20(ctx, luck=0):
    if luck:
        await ctx.send(min(random.randint(1, 21), random.randint(1, 21)) if int(luck) < 0
                       else max(random.randint(1, 21), random.randint(1, 21)))
    else:
        await ctx.send(random.randint(1, 21))


@bot.command(name='init')
async def init(ctx, player_amount):
    pass

TOKEN = "MTIyMzk2Nzk0ODAyNTIzNzUwNA.GJD1aq.fN831iWHFIT8Gn4S6e43SSlJgdBtQQDFce8dYA"

bot.run(TOKEN)
