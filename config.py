TOKEN = "MTIyNzYyMjIzMDcyNTQ5Njg3Mg.GbfI16.NPQz_AtmRmNIPbowhqrUtb5K7s9hpIS15MDu54"

COMMAND_PREFIX = '!'
DEFAULT_WEIGHT = 5
DEFAUL_MAX_INVENTORY_WEIGHT = 30
HP_TO_UP_LEVEL = 20


class Eng:
    def help(self) -> str:
        return f"""To create character type {COMMAND_PREFIX}create
        
        To delete your character type {COMMAND_PREFIX}delete
        
        To roll dice type {COMMAND_PREFIX}roll <whatever you like to roll>
        For example {COMMAND_PREFIX}roll 2d20 will roll two d20 and show you the result
        
        To test your ability to do something type {COMMAND_PREFIX}check <attribute> <number bigger than 0 if you have advantage, less than 0 if you in disadvantage or nothing if you haven't any of them>
        
        To see your inventory type {COMMAND_PREFIX}inventory\n\nTo take something to your inventory type {COMMAND_PREFIX}take <item>
        
        To use something from your inventory type {COMMAND_PREFIX}use <item>
        
        To throw something from your inventory type {COMMAND_PREFIX}throw <item>
        
        To see all information about your character type {COMMAND_PREFIX}character"""

    def roll(self) -> tuple[str, str]:
        return '- are your rolls', '- and there is sum of your rolls'

    def create(self) -> tuple[str, str, str]:
        return (f"You already have started adding you character! Type {COMMAND_PREFIX}end to finish",
                f"You started creating your character. Type {COMMAND_PREFIX}name to set name to your character",
                "You have got a character!")

    def name(self) -> tuple[str, str]:
        return ("You are not adding or editing character!",
                f"""Successful! 
                Now you should tell me about your character by typing
                {COMMAND_PREFIX}about <your backstory>""")

    def about(self) -> tuple[str, str, str]:
        return ("You are not adding or editing character!", "You have changeв your character's description",
                f"""Successful! Now you should set attributes for your character by typing 
                {COMMAND_PREFIX}attributes""")

    def attributes(self, attr: str, nums: list[int]) -> tuple[str, str, str, str]:
        return ("You not adding character!", f"You already have {attr}. You can't change it!",
                f"You already have {attr}. You can't change it!",
                f"""You have {' '.join(map(str, nums))}.
                Please assign them to your attributes by typing
                {COMMAND_PREFIX}set <num for strength> <num for dexterity> <num for constitution> <num for intelligence> <num for wisdom> <num for charisma>""")

    def set(self) -> tuple[str, str, str, str, str]:
        return (
            "You are not adding or editing character!", "You haven't got attributes!", "You've done something wrong!",
            "Cool! You changed your character's attributes",
            f"Perfect! Type {COMMAND_PREFIX}end to finish creating your character. Good luck")

    def end(self) -> tuple[str, str, str, str, str]:
        return ("You are not adding or editing character!", "You haven't chosen name",
                "You haven't set attributes", "Character has been added!", "Character has been edited!")

    def edit(self):
        return (f"You already have started adding your character! Type {COMMAND_PREFIX}end to finish",
                f"You already have started editing your character! Type {COMMAND_PREFIX}end to finish",
                "You haven't got character", "You start editing your character")

    def delete(self):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "You haven't got a character", "Character has been deleted")

    def take(self):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "You haven't got any character!", "You can't take it. Your inventory is too heavy")

    def give(self, item: str):
        return ("You should finish adding your character first", "You should finish editing your character first",
                f"Something wrong, maybe you don't know who you want to give the {item} to",
                "You can't take it. Your inventory is too heavy")

    def take_(self, name: str, item: str):
        return f"{name} just obtained {item}"

    def check(self):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "Create your character first", "Something wrong, try again", "- your rolls", "-your result")

    def use(self, item: str):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "Create your character first", f"You haven't got {item}", f"You have used {item}")

    def throw(self, item: str):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "Create your character first", f"You haven't got {item}", f"You have thrown {item}")

    def inventory(self):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "Create your character first", "You haven`t got nothing")

    def xp(self):
        return "You haven't got any character"

    def character(self, character):
        return (
            "You do not have character",
            f"Your character's name is {character.name}",
            f"Your character's backstory is {character.about}",
            f"Your character's attributes are {character.strength}{character.dexterity} {character.constitution} {character.intelligence} {character.wisdom} {character.charisma}",
            "You haven't got nothing",
            f"Your inventory is {', '.join(character.inventory.strip('*').split('*'))} with weight {character.inventory_weight} (max weight = {character.max_inventory_weight})",
            f"Your level is {character.level} and you have {character.xp}xp"
        )


class Ru(Eng):
    def help(self) -> str:
        return f"""Чтобы создать персонажа, наберите {COMMAND_PREFIX}create

        Чтобы удалить персонажа, воспользуйтесь командой {COMMAND_PREFIX}delete

        Команда для броска игральных костей: {COMMAND_PREFIX}roll <кости, которые вы хотите бросить>
        Например {COMMAND_PREFIX}roll 2d20 сымитирует бросок двух 20-тигранных кубиков и покажет вам результат

        Чтобы проверить возможность персонажа совершить какое-либо действие введите {COMMAND_PREFIX}check <характеристика> <число, большее 0, если проверка с преимуществом, меньше 0, если с помехой. Если ни того, ни другого нет, ничего писать не нужно>
        
        Для взаимодействия с инвентарем есть команды:
        {COMMAND_PREFIX}inventory (показывает инвентарь),
        {COMMAND_PREFIX}take <предмет> (получить предмет),
        {COMMAND_PREFIX}give <предмет> (передать предмет),
        {COMMAND_PREFIX}use <предмет> (использовать предмет),
        {COMMAND_PREFIX}throw <предмет> (выбросить предмет)

        Для того,чтобы посмотреть информацию о персонаже, необходимо ввести {COMMAND_PREFIX}character"""

    def roll(self) -> tuple[str, str]:
        return '- значения ваших бросков', '- а также их сумма'

    def create(self) -> tuple[str, str, str]:
        return (f"Вы уже начали создавать персонажа! Наберите {COMMAND_PREFIX}end, чтобы завершить процесс создавания",
                f"Вы начали создавать персонажа. Для выбора имени введите {COMMAND_PREFIX}name <имя персонажа>",
                "У вас уже есть персонаж!")

    def name(self) -> tuple[str, str]:
        return ("Вы не создаете и не изменяете персонажа!",
                f"""Супер! 
                Теперь расскажите о вашем персонаже при помощи команды
                {COMMAND_PREFIX}about <предыстория персонажа>""")

    def about(self) -> tuple[str, str, str]:
        return (
        "Вы не создаете и не изменяете персонажа!", "Вы изменили вашу предысторию (как бы странно это не звучало)",
        f"""Отлично! Теперь вам надо настроить характеристики вашего персонажа при помощи этой команды: 
                {COMMAND_PREFIX}attributes""")

    def attributes(self, attr: str, nums: list[int]) -> tuple[str, str, str]:
        return ("Вы не создаете персонажа", f"У вас уже есть набор характеристик ({attr}). Вы не можете их изменить",
                f"""Ваш набор значений: {' '.join(map(str, nums))}.
                Пожалуйста, распределите их в соответствии с вашими предпочтениями между вашими характеристиками
                {COMMAND_PREFIX}set <значение для силы> <значение для ловкости> <значение для выносливости> <значение для интеллекта> <значение для мудрости> <значение для харизмы>""")

    def set(self) -> tuple[str, str, str, str, str]:
        return (
            "Вы не создаете и не изменяете персонажа!",
            f"Сначала получите значения для характеристик ({COMMAND_PREFIX}attributes)", "Упс, что-то пошло не так",
            "Отличный выбор!",
            f"Идеально. Завершите создание персонажа командой {COMMAND_PREFIX}end. Удачи!")

    def end(self) -> tuple[str, str, str, str, str]:
        return ("Вы не создаете и не изменяете персонажа!", f"Вы не выбрали имя ({COMMAND_PREFIX}name <имя персонажа>)",
                f"Я не знаю, в чем ваши сильные и слабые стороны ({COMMAND_PREFIX}set <значение для силы> <значение "
                f"для ловкости> <значение для выносливости> <значение для интеллекта> <значение для мудрости> "
                f"<значение для харизмы>)", "Персонаж добавлен", "Персонаж изменен")

    def edit(self):
        return (f"Вы уже начали создавать персонажа! Наберите {COMMAND_PREFIX}end, чтобы завершить процесс создавания",
                f"Вы уже начали изменять персонажа! Наберите {COMMAND_PREFIX}end, чтобы завершить процесс создавания",
                "К сожалению, я не могу найти вашего персонажа", "Вы начали изменять своего персонажа")

    def delete(self):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                "Для начала создайте своего персонажа!", "Персонаж был удален")

    def take(self):
        return ("You should finish adding your character first", "You should finish editing your character first",
                "Для начала создайте своего персонажа!", "Это невозможно, на вас и так слишком много тяжестей")

    def give(self, item: str):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                f"Что-то пошло не так. Может быть вы не знаете кому вы хотите передать {item}?",
                f"К сожалению это невозможно. {item} слишком тяжелый для этого")

    def take_(self, name: str, item: str):
        return f"{name} только что получил {item}"

    def check(self):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                "Для начала создайте своего персонажа!", "Что-то пошло не так(",
                "- значения ваших бросков", "- ваш результат")

    def use(self, item: str):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                "Для начала создайте своего персонажа!", f"You haven't got {item}", f"You have used {item}")

    def throw(self, item: str):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                "Для начала создайте своего персонажа!",
                f"Вы осматриваете свои карманы, но не находите там того, что искали", f"Вы выбросили {item}")

    def inventory(self):
        return ("Сначала завершите создание вашего персонажа", "Сначала завершите редактирование вашего персонажа",
                "Для начала создайте своего персонажа!", "У вас ничего нет")

    def xp(self):
        return "У вас нет персонажа!"

    def character(self, character):
        return (
            "У вас нет персонажа!"
            f"Имя вашего персонажа: {character.name}",
            f"Предыстория вашего персонажа: {character.about}",
            f"Характеристики {character.strength}{character.dexterity} {character.constitution} {character.intelligence} {character.wisdom} {character.charisma}",
            "Ваш инвентарь пуст",
            f"Содержимое вашего инвентаря -  {', '.join(character.inventory.strip('*').split('*'))} with weight {character.inventory_weight} (max weight = {character.max_inventory_weight})",
            f"У вас {character.level} уровень и {character.xp} опыта"
        )


LANG = Eng()
