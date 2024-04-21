from data import players

CHR_CLASSES = [8, 12, 10, 6, 8, 8, 8, 8, 8, 10, 8, 10, 6]


class Character:
    def __init__(self, name, about, hp, strength, dexterity, constitution, intellegence, wisdom, charisma, modifier, secondary_modifier, level, xp, chr_class, armor):
        self.name = name
        self.max_hp =hp
        self.hp = self.max_hp
        self.attribute = [strength, dexterity, constitution, intellegence, wisdom, charisma]
        self.secondary = (modifier, secondary_modifier)
        self.about = about
        self.level = level
        self.xp = xp
        self.armor = armor
        self.chr_class = chr_class

    def get_db_copy(self):
        player = players.Player()
        player.name = self.name
        player.about = self.about
        player.hp = self.max_hp
        player.strength, player.dexterity, player.constitution, player.intellegence, \
            player.wisdom, player.charisma = self.attribute
        player.modifier, player.secondary_modifier = self.secondary
        player.level = self.level
        player.xp = self.xp
        player.chr_class = self.chr_class
        player.armor = self.armor
        return player

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)
        return self.is_alive()

    def heal(self, heal):
        self.hp = min(self.hp + heal, self.max_hp)

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def set_max_hp(self, new_xp):
        self.max_hp = new_xp

    def is_alive(self):
        return self.hp != 0

    def kill(self):
        self.hp = 0

    def set_history(self, new_history):
        self.about = new_history

    def get_history(self):
        return self.about

    def level_up(self, up):
        self.level += up
        self.max_hp += CHR_CLASSES[self.chr_class]
        self.xp = 0

    def get_level(self):
        return self.level

    def set_level(self, new_level):
        self.level = new_level

    def check(self, is_in_advantage: bool, is_in_disadvantage: bool):
        pass
