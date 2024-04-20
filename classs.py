CHR_CLASSES = [8, 12, 10, 6, 8, 8, 8, 8, 8, 10, 8, 10, 6]

class Character:
    def __init__(self, name, st, dex, cn, intellegence, wsd, charisma, modifier, about, armor, inventory, chr_class):
        self.name = name
        self.max_hp = CHR_CLASSES[chr_class]
        self.hp = self.max_hp
        self.skills = skills
        self.about = about
        self.level = 0
        self.armor = armor
        self.inventory = inventory
        self.chr_class = chr_class

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

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

    def get_level(self):
        return self.level

    def set_level(self, new_level):
        self.level = new_level

    def check(self, is_in_advantage:bool, is_in_disadvantage:bool):
        pass

