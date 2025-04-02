from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self, monster):
        attack_result = self.weapon.attack()
        print(attack_result)
        print("Монстр побежден!")

class Monster:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца с начальным оружием
fighter = Fighter(sword)

# Создаем монстра
monster = Monster("Огр")

# Бой с мечом
print("Боец выбирает меч.")
fighter.fight(monster)

# Меняем оружие на лук
print("\nБоец выбирает лук.")
fighter.change_weapon(bow)
fighter.fight(monster)