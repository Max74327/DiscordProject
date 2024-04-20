import discord
import classs
from discord.ext import commands
import random
import logging
from data import db_session

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
db_session.global_init("db/players.db")

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


async def save(character):
    pass


async def load(character):
    pass


async def create(client):
    character = classs.Character(name=input(), about=input(), chr_class=int(input()), skills=[random.randint(9, 15) for i in range(6)])


TOKEN = ""

# bot.run(TOKEN)
