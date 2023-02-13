class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)


villager = NPC("Bob", 100, 12)
villager.name  # Bob
villager.hp  # 100
villager.level  # 12
villager.speak()  # "I heard there were monsters running around last night!".