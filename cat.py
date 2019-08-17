from random import randint
from typing import Tuple

from animal import Animal


class Cat(Animal):
    __sounds = ["Meow", "Nyan", "Meo", "Mjau"]

    def __init__(self, name: str):
        sound = Animal._choose_random_sound(Cat.__sounds)
        health = 9
        damage = 6
        defence = 2
        super().__init__(name, sound, health, damage, defence)

    def special_attack(self) -> Tuple[int, str]:
        return randint(1, self._damage), "clawed"

    def get_name(self) -> str:
        return f"{self._name} (the cat)"
