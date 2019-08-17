from animal import Animal


class Dog(Animal):
    __sounds = ["Woof", "Ruff", "Arf", "Waf"]

    def __init__(self, name: str):
        sound = Animal._choose_random_sound(Dog.__sounds)
        health = 12
        damage = 5
        defence = 1
        special_attack_name = "back-kicked"
        super().__init__(name, sound, health, damage, defence, special_attack_name)

    def get_name(self) -> str:
        return f"{self._name} (the dog)"
