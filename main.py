from config import *
import discord
from discord.ext import commands
import logging
import random
from data import db_session
from random import randint

db_session.global_init("db/players.db")
from data import db_session
from data.characters import Character

db_session.global_init("db/players.db")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


@bot.command(name='help_me')
async def help(ctx):
    await ctx.send(LANG.help())


@bot.command(name='roll')
async def roll(ctx, data):
    l = LANG.roll()
    output = list()
    for _ in range(int(data[:data.index('d')] or 1)):
        output.append(random.randint(1, int(data[data.index('d') + 1:])))
    if len(output) > 1:
        await ctx.send(f'{" ".join(map(str, output))} {l[0]}\n{str(sum(output))} {l[1]}')
    else:
        await ctx.send(f'{output[0]}')


adding = {}
editing = {}


@bot.command(name='create')
async def create_character(ctx):
    l = LANG.create()
    player = ctx.author.name
    db_sess = db_session.create_session()
    if player in adding:
        await ctx.send(l[0])
    else:
        exist = False
        for user in db_sess.query(Character).all():
            if user.username == player:
                exist = True
        if not exist:
            adding[player] = ["", "", "", "", "", "", "", "", "", ""]
            await ctx.send(l[1])
            # написать help
        else:
            await ctx.send(l[2])


@bot.command(name="name")
async def name(ctx, name):
    l = LANG.name()
    player = ctx.author.name
    if player not in adding and player not in editing:
        await ctx.send(l[0])
        return
    if player in editing:
        editing[player][0] = name
        await ctx.send(l[1])
        return
    adding[player][0] = name
    await ctx.send(l[2])


@bot.command(name="about")
async def about(ctx, about):
    l = LANG.about()
    player = ctx.author.name
    if player not in adding and player not in editing:
        await ctx.send(l[0])
        return
    if player in editing:
        editing[player][1] = about
        await ctx.send(l[1])
        return
    adding[player][1] = about
    await ctx.send(l[2])


'''
@bot.command(name="class")
async def clss(ctx, clss):
    player = ctx.author.name
    if player not in adding:
        await ctx.send("You are not adding character!")
    else:
        adding[player][2] = clss'''


@bot.command(name="attributes")
async def get_attributes(ctx):
    player = ctx.author.name
    numbers: list[int] = []
    for i in range(6):
        first, second, third, fourth = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
        numbers.append(first + second + third + fourth - min(first, second, third, fourth))
    l = LANG.attributes(adding[player][9], numbers)
    if player not in adding and player not in editing:
        await ctx.send(l[0])
        return
    if player in adding and adding[player][9]:
        await ctx.send(l[1])
        return
    if player in editing:
        await ctx.send(l[2])
        return
    adding[player][9] = numbers
    await ctx.send(l[3])


@bot.command(name="set")
async def set_attributes(ctx, strength, dexterity, constitution, intelligence, wisdom, charisma):
    player = ctx.author.name
    l = LANG.set()
    if player not in adding and player not in editing:
        await ctx.send(l[0])
        return
    if not adding[player][9]:
        await ctx.send(l[1])
        return
    if sorted(adding[player][9]) != sorted(
            list(map(int, [strength, dexterity, constitution, intelligence, wisdom, charisma]))):
        await ctx.send(l[2])
        return
    if player in editing:
        editing[player][3], editing[player][4], editing[player][5], editing[player][6], editing[player][7], \
            editing[player][
                8] = strength, dexterity, constitution, intelligence, wisdom, charisma
        await ctx.send(l[3])
        return
    adding[player][3], adding[player][4], adding[player][5], adding[player][6], adding[player][7], adding[player][
        8] = strength, dexterity, constitution, intelligence, wisdom, charisma
    await ctx.send(l[4])


@bot.command(name="end")
async def end(ctx):
    l = LANG.end()
    player = ctx.author.name
    if player not in adding and player not in editing:
        await ctx.send(l[0])
        return
    if player in adding:
        if not adding[player][0]:
            await ctx.send(l[1])
            return
        # player[2] зарезервировано под класс
        if not adding[player][3]:
            await ctx.send(l[2])
            return
        if player in adding:
            character = Character()
            character.name = adding[player][0]
            character.username = player
            character.about = adding[player][1]
            '''character.clss = adding[player][2]'''
            character.strength = int(adding[player][3])
            character.dexterity = int(adding[player][4])
            character.constitution = int(adding[player][5])
            character.intelligence = int(adding[player][6])
            character.wisdom = int(adding[player][7])
            character.charisma = int(adding[player][8])
            character.inventory = '*'
            character.inventory_weight = 0
            character.level = 0
            # КРАЙНЕ СТРАННАЯ ФОРМУЛА!!
            character.max_inventory_weight = DEFAUL_MAX_INVENTORY_WEIGHT + character.strength
            del adding[player]
            db_sess = db_session.create_session()
            db_sess.add(character)
            db_sess.commit()
            await ctx.send(l[3])
            return
    character = Character()

    character.name = editing[player][0]
    character.username = player
    character.about = editing[player][1]
    '''character.clss = adding[player][2]'''
    character.strength = int(editing[player][3])
    character.dexterity = int(editing[player][4])
    character.constitution = int(editing[player][5])
    character.intelligence = int(editing[player][6])
    character.wisdom = int(editing[player][7])
    character.charisma = int(editing[player][8])
    character.inventory = editing[player][10]
    character.inventory_weight = editing[player][11]
    character.level = editing[player][12]
    character.max_inventory_weight = DEFAUL_MAX_INVENTORY_WEIGHT + character.strength
    # КРАЙНЕ СТРАННАЯ ФОРМУЛА!!
    del editing[player]
    db_sess = db_session.create_session()
    db_sess.query(character).filter(character.username == player).delete()
    db_sess.add(character)
    db_sess.commit()
    await ctx.send(l[4])


@bot.command(name='edit')
async def edit(ctx):
    l = LANG.edit()
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
        return
    editing[player] = [character.name, character.about, "", character.strength, character.dexterity,
                       character.constitution, character.intelligence, character.wisdom, character.charisma,
                       (character.strength, character.dexterity, character.constitution, character.intelligence,
                        character.wisdom, character.charisma), character.inventory, character.inventory_weight,
                       character.level]
    await ctx.send(l[3])


@bot.command(name='delete')
async def delete(ctx):
    l = LANG.delete()
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
        return
    db_sess.query(Character).filter(Character.username == player).delete()
    db_sess.commit()
    await ctx.send(l[3])


@bot.command(name='take')
async def take(ctx, item):
    character = None
    l = LANG.take()
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return

    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
    elif character.inventory_weight + DEFAULT_WEIGHT > character.max_inventory_weight:
        await ctx.send(l[3])
    else:
        character.inventory += item + "*"
        character.inventory_weight += DEFAULT_WEIGHT
        await ctx.send(LANG.take_(character.name, item))
    db_sess.commit()


@bot.command(name="give")
async def give(ctx, player, item):
    character = None
    l = LANG.give(item)
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
    elif character.inventory_weight + DEFAULT_WEIGHT > character.max_inventory_weight:
        await ctx.send(l[3])
    else:
        character.inventory += item + "*"
        character.inventory_weight += DEFAULT_WEIGHT
        await ctx.send(LANG.take_(character.name, item))

    db_sess.commit()


@bot.command(name='check')
async def check(ctx, attribute, luck=0):
    l = LANG.check()
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    db_sess.commit()
    if not character:
        await ctx.send(l[2])
        return
    match attribute:
        case 'strength':
            modifier = (character.strength - 10) // 2
        case 'dexterity':
            modifier = (character.dexterity - 10) // 2
        case 'constitution':
            modifier = (character.constitution - 10) // 2
        case 'intelligence':
            modifier = (character.intelligence - 10) // 2
        case 'wisdom':
            modifier = (character.wisdom - 10) // 2
        case 'charisma':
            modifier = (character.charisma - 10) // 2
        case 'сила':
            modifier = (character.strength - 10) // 2
        case 'ловкость':
            modifier = (character.dexterity - 10) // 2
        case 'выносливость':
            modifier = (character.constitution - 10) // 2
        case 'интеллект':
            modifier = (character.intelligence - 10) // 2
        case 'мудрость':
            modifier = (character.wisdom - 10) // 2
        case 'харизма':
            modifier = (character.charisma - 10) // 2
        case _:
            await ctx.send(l[3])
            return
    rolls = [randint(1, 20)]
    if luck:
        rolls += [randint(1, 20)]
    await ctx.send(' '.join(map(str, rolls)) + l[4])
    await ctx.send(str(max(rolls) if luck > 0 else min(rolls) + modifier) + l[5])


@bot.command(name='use')
async def use(ctx, item):
    l =LANG.use(item)
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
        return
    if "*" + item + "*" not in character.inventory:
        await ctx.send(l[3])
        return
    index = character.inventory.index("*" + item + "*")

    character.inventory = character.inventory[:index] + "*" + character.inventory[index + len(item) + 2:]
    character.inventory_weight -= DEFAULT_WEIGHT
    await ctx.send(l[4])
    db_sess.commit()


@bot.command(name='throw')
async def throw(ctx, item):
    l =LANG.throw(item)
    # в use могут быть когда-то в будующем взаимодействия с характеристиками
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    if not character:
        await ctx.send(l[2])
        return
    if "*" + item + "*" not in character.inventory:
        await ctx.send(l[3])
        return
    index = character.inventory.index("*" + item + "*")

    character.inventory = character.inventory[:index] + "*" + character.inventory[index + len(item) + 2:]
    character.inventory_weight -= DEFAULT_WEIGHT
    await ctx.send(l[4])
    db_sess.commit()


@bot.command(name="inventory")
async def show(ctx):
    l = LANG.inventory()
    player = ctx.author.name
    if player in adding:
        await ctx.send(l[0])
        return
    if player in editing:
        await ctx.send(l[1])
        return
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
    db_sess.commit()
    if not character:
        await ctx.send(l[2])
        return
    if character.inventory == "*":
        await ctx.send(l[3])
        return
    stroka = ''
    for symb in character.inventory:
        stroka += symb if symb != "*" else " "
    await ctx.send(stroka)


@bot.command(name='character')
async def character(ctx):
    player = ctx.author.name
    character = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character = user
            break
    l = LANG.character(character)
    if not character:
        await ctx.send(l[0])
        return
    await ctx.send(l[1])
    await ctx.send(l[2])
    await ctx.send(l[3])
    if character.inventory == "*":
        await ctx.send(l[4])
    else:
        await ctx.send(l[5])
    await ctx.send(l[6])


@bot.command(name="xp")
async def xp(ctx, xp):
    player = ctx.author.name
    character_ = ''
    db_sess = db_session.create_session()
    for user in db_sess.query(Character).all():
        if user.username == player:
            character_ = user
    if not character_:
        await ctx.send(LANG.xp())
        return
    if character_.xp + xp >= HP_TO_UP_LEVEL:
        up = (character_.xp + xp) // HP_TO_UP_LEVEL
        character_.xp = (character_.xp + xp) // HP_TO_UP_LEVEL
        level_up(character_, up)
        return
    character_.hp += xp
    db_sess.commit()


def level_up(character, up):
    pass
    # не команда через дс, тут надо добавить уровень персонажу и ещё чего-то в зависимости от класса


bot.run(TOKEN)
