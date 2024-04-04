from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        return self.weapon.attack()

# Класс монстра
class Monster:
    pass

# Демонстрация боя
def game_demo():
    # Создаем бойца с мечом
    fighter = Fighter(Sword())
    print("Боец выбирает меч.")
    print(fighter.fight())

    # Результат боя
    print("\nМонстр побежден!")

    # Смена оружия на лук
    fighter.change_weapon(Bow())
    print("\nБоец выбирает лук.")
    print(fighter.fight())

    # Результат боя
    print("\nМонстр побежден!")

game_demo()
