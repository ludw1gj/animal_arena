from random import shuffle

from animal import Animal


class Arena:
    def __init__(self, cat, dog):
        self.dog = dog
        self.cat = cat
        pass

    def fight(self) -> None:
        contenders = [self.cat, self.dog]
        shuffle(contenders)

        print(Arena.__gen_enter_the_pit_text(contenders[0]))
        print(Arena.__gen_enter_the_pit_text(contenders[1]))

        while self.cat.is_alive() and self.dog.is_alive():
            shuffle(contenders)
            Arena.__animal_attack(contenders[0], contenders[1])

        winner_name = self.cat.get_name() if self.cat.is_alive() else self.dog.get_name()
        print(f"\n{winner_name} has won the battle!")

    @staticmethod
    def __gen_enter_the_pit_text(animal: Animal) -> str:
        return f"{animal.speak()}! {animal.get_name()} has entered the area!"

    @staticmethod
    def __animal_attack(attacker: Animal, attacked: Animal) -> None:
        damage = attacker.attack()
        attacked.receive_damage(damage)
        print(f"\n{attacker.get_name()} attacked {attacked.get_name()} and dealt {damage} damage.")
        if attacked.is_alive():
            print(f"{attacked.get_name()} now has {attacked.get_health()} HP left.")
        else:
            print(f"{attacked.get_name()} has been killed.")

