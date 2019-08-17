from typing import Tuple

from animal import Animal


class Cat(Animal):
    __sounds = ["Meow", "Nyan", "Meo", "Mjau"]

    def __init__(self, name: str):
        sound = Animal._choose_random_sound(Cat.__sounds)
        health = 10
        damage = 6
        defence = 1
        super().__init__(name, sound, health, damage, defence)

    def special_attack(self) -> Tuple[int, str]:
        return self.__damage * 2, "slash"

    def get_name(self) -> str:
        return f"{self._name} (the cat)"
