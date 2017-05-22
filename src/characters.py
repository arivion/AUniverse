"""

"""
# TODO: name IO somehow (file/input options?)

import random


def help_info():
    print("Usage:")
    print("\tships: pair up characters (with a chance of some being single)")
    print("\tchoose: pick a character at random")
    print("\thelp: print usage information")
    print("\tquit: exit the program")


def shipping(names: tuple):
    names_list = list(names)
    pairs = len(names_list) // 2
    for pair in range(0, pairs):
        name = names_list[random.randint(0, len(names_list)-1)]
        names_list.remove(name)
        partner = names_list[random.randint(0, len(names_list)-1)]
        names_list.remove(partner)
        if random.randint(0, 9) == 0:
            print(name + " and " + partner + " are both single.")
        else:
            print(name + " and " + partner + " are together.")
    if len(names_list) != 0:
        print(names_list[0] + "")


def main():
    random.seed(None)
    names = ("Jack", "Lana", "Scott", "Mary", "Wren", "Alice",
             "Elijah", "Claire", "Silas", "Emily", "Teddy", "Sam")

    while 1:
        command = input("> ").lower()
        if command == "quit":
            break
        elif command == "help":
            help_info()
        elif command == "ships":
            shipping(names)
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        else:
            print("Whoops, that's not right!")
            help_info()


main()
