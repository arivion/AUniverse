"""
:file: universe.py
Application to help brainstorm character relationships and loyalties

:author: Alexia Christie
"""
import random


def help_info():
    """
    Print usage information to terminal
    :return: None
    """
    print("Usage:")
    print("  ships: pair up characters (with a single character if there is an odd number)")
    print("  choose: pick a character at random")
    print("  names: display list of names")
    print("  help: print usage information")
    print("  quit: exit the program")


def shipping(characters: tuple):
    """
    Pairs up characters into couples
    :param characters:
    :return:
    """
    char_list = list(characters)
    pairs = len(char_list) // 2

    for pair in range(0, pairs):
        # After choosing a character, remove them from the list to prevent redundancy.
        char = char_list[random.randint(0, len(char_list)-1)]
        char_list.remove(char)
        partner = char_list[random.randint(0, len(char_list)-1)]
        char_list.remove(partner)
        # Display results
        print(char + " and " + partner + " are together.")

    if len(char_list) != 0:
        print(char_list[0] + " is single.")


def main():
    random.seed(None)

    names = tuple(input("Enter names separated by commas: ").split(","))
    for name in names:
        name.lstrip().rstrip()

    while 1:
        command = input("> ").lower()
        if command == "quit":
            break
        elif command == "help":
            help_info()
        elif command == "ships":
            shipping(tuple(names))
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        elif command == "names":
            print(list(names))
        else:
            print("Whoops, that's not right!")
            help_info()


main()
