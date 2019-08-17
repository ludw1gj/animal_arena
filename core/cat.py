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
