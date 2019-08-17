from core.arena import Arena
from core.cat import Cat
from core.dog import Dog


def start_game():
    cat = Cat("Grumpy")
    dog = Dog("Max")
    arena = Arena(cat, dog)

    print("Game started...\n")
    arena.fight()


start_game()
