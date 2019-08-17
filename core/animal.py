from abc import abstractmethod
from random import randint
from typing import List, Tuple


class Animal:
    def __init__(self, name: str, sound: str, health: int, damage: int, defence: int, special_attack_name: str):
        self._name = name
        self._health = health
        self._sound = sound
        self._damage = damage
        self._defence = defence
        self._is_alive = True
        self._special_attack_name = special_attack_name

    def _is_dead_error(self, action) -> None:
        if not self._is_alive:
            raise Exception(f"cannot {action} when dead")

    def get_health(self):
        return self._health

    def speak(self) -> str:
        self._is_dead_error("speak")
        return self._sound

    def attack(self) -> Tuple[int, str]:
        self._is_dead_error("attack")
        return randint(1, self._damage), "attacked"

    def receive_damage(self, damage: int) -> bool:
        self._is_dead_error("receive damage")

        self._health -= damage - randint(0, self._defence)
        if self._health <= 0:
            self._is_alive = False
            self._health = 0
        return self._is_alive

    def is_alive(self):
        return self._is_alive

    def special_attack(self) -> Tuple[int, str]:
        self._is_dead_error("special attack")
        return randint(1, self._damage) * 2, self._special_attack_name

    @abstractmethod
    def get_name(self) -> str:
        pass

    @staticmethod
    def _choose_random_sound(sounds: List[str]) -> str:
        rand_index = randint(0, len(sounds) - 1)
        return sounds[rand_index]
