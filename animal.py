from abc import abstractmethod
from random import randint
from typing import List, Tuple


class Animal:
    def __init__(self, name: str, sound: str, health: int, damage: int, defence: int):
        self._name = name
        self.__health = health
        self.__sound = sound
        self.__damage = damage
        self.__defence = defence
        self.__is_alive = True

    def _is_dead_error(self, action) -> None:
        if not self.__is_alive:
            raise Exception(f"cannot {action} when dead")

    def get_health(self):
        return self.__health

    def speak(self) -> str:
        self._is_dead_error("speak")
        return self.__sound

    def attack(self) -> int:
        self._is_dead_error("attack")
        return randint(1, self.__damage)

    def receive_damage(self, damage: int) -> bool:
        self._is_dead_error("receive damage")

        self.__health -= damage
        if self.__health <= 0:
            self.__is_alive = False
            self.__health = 0
        return self.__is_alive

    def is_alive(self):
        return self.__is_alive

    @abstractmethod
    def special_attack(self) -> Tuple[int, str]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @staticmethod
    def _choose_random_sound(sounds: List[str]) -> str:
        rand_index = randint(0, len(sounds) - 1)
        return sounds[rand_index]
