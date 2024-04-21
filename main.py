import discord
import classs
from discord.ext import commands
import random
import sqlite3
import logging
from data import db_session

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
db_session.global_init("db/players.db")
con = sqlite3.connect("db/players.db")
cur = con.cursor()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
active_characters = {}
bot = commands.Bot(command_prefix='#', intents=intents)


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


def start(ctx):
    active_characters[ctx.message.author.id] = 'master'


async def save(ctx):
    try:
        active_characters[ctx.messege.author.id]
    except Exception:
        await ctx.send('You are not in the session')
        return
    db_sess = db_session.create_session()
    db_sess.add(active_characters[ctx.messege.author.id].get_db_copy())
    db_sess.commit()
    del active_characters[ctx.messege.author.id]


async def load(ctx, character):
    result = cur.execute(f"""SELECT * FROM players WHERE name = {character}""").fetchall()
    active_characters[ctx.messege.author.id] = classs.Character(*result[1:])


async def create(ctx):
    await ctx.send('Enter character`s name')
    name = input()  # ___________________________________________________________!!!! Find the way this should work !!!!
    result = cur.execute("""SELECT name FROM players""").fetchall()
    while name in result:
        name = input() # ________________________________________________________!!!! Find the way this should work !!!!
    everithing_else = []
    active_characters[ctx.messege.author.id] = classs.Character(name=name, *everithing_else)


TOKEN = ""

# bot.run(TOKEN)
