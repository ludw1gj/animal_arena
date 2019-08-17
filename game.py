from arena import Arena
from cat import Cat
from dog import Dog


def start_game():
    cat = Cat("Grumpy")
    dog = Dog("Max")
    arena = Arena(cat, dog)

    print("Game started...\n")
    arena.fight()


start_game()
