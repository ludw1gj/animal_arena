from typing import Tuple

from animal import Animal


class Dog(Animal):
    __sounds = ["Woof", "Ruff", "Arf", "Waf"]

    def __init__(self, name: str):
        sound = Animal._choose_random_sound(Dog.__sounds)
        health = 13
        damage = 5
        defence = 3
        super().__init__(name, sound, health, damage, defence)

    def special_attack(self) -> Tuple[int, str]:
        return self.__damage * 2, "back kick"

    def get_name(self) -> str:
        return f"{self._name} (the dog)"
