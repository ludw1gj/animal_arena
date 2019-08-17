from random import random

from core.animal import Animal


class Cat(Animal):
    __sounds = ["Meow", "Nyan", "Meo", "Mjau"]

    def __init__(self, name: str):
        sound = Animal._choose_random_sound(Cat.__sounds)
        health = 9
        damage = 6
        defence = 2
        special_attack_name = "clawed"
        super().__init__(name, sound, health, damage, defence, special_attack_name)

    def get_name(self) -> str:
        return f"{self._name} (the cat)"

    def receive_damage(self, damage: int) -> bool:
        _ = super().receive_damage(damage)
        if not self.is_alive and random() < 0.2:
            # nine lives ability
            self._health = 1
            self._is_alive = True
            print(f"{self._name} landed on his/her feet.")
            return True
        return self.is_alive
