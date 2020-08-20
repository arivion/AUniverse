"""
:file: universe.py
Application to help brainstorm character relationships and loyalties

:author: Alexia Christie
"""
import random
import sys


def help_info():
    """
    Print usage information to terminal
    :return: None
    """
    print("Usage:")
    print("  ships: pair up characters (with a single character if there is an odd number)")
    print("  choose: pick a character at random")
    print("  assign: assign characters to roles")
    print("  names: display list of names")
    print("  help: print usage information")
    print("  quit: exit the program")


def shipping(characters: tuple):
    """
    Pairs up characters into couples
    :param characters:
    :return: a dictionary mapping character:character
    """
    pair_map = {}

    while True:
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
            pair_map['char'] = partner

        if len(char_list) != 0:
            print(char_list[0] + " is single.")
            pair_map[char_list[0]] = 'Nobody :('

        roll_again = input('Roll again? : ')
        if (not roll_again.lower() == 'y') and (not roll_again.lower() == 'yes'):
            break

    return pair_map


def assign(characters: tuple):
    """
    Assigns characters to roles
    :param characters: a tuple containing the names of the characters
    :return: a dictionary mapping character:role
    TODO: be able to limit automatic selection to a certain subset
    """
    role_map = {}

    while True:
        char_list = list(characters)

        while True:

            role = input('Enter a role you want randomly assigned '
                         'OR the name of a character you want to assign, or reassign, a role to: ')

            if role in characters:
                character = role
                role = input('Assign a role for [' + role + ']')
            else:
                character = char_list[random.randint(0, len(char_list)-1)]
            role_map[character] = role
            char_list.remove(character)
            print(character + ' has the following role: ' + role)
            print('Remaining characters: ' + str(char_list))
            if not char_list:
                break
            print('\n')

        for pair in role_map:
            print(pair + " : " + role_map.get(pair))
        roll_again = input('Roll again? : ')
        if (not roll_again.lower() == 'y') and (not roll_again.lower() == 'yes'):
            break

    return role_map


def main():
    random.seed(None)

    if len(sys.argv) == 1:
        print("Oops! This needs a file listing character names to run. "
              "Expected usage: python universe.py [character file]")
        exit(1)

    names_unstripped = open(sys.argv[1])
    names = tuple(s.rstrip() for s in tuple(names_unstripped))
    ship_dict = {}
    role_dict = {}

    while 1:
        command = input("\n> ").lower()
        if command == "quit":
            break
        elif command == "help":
            help_info()
        elif command == "ships":
            ship_dict = shipping(names)
        elif command == "assign":
            role_dict = assign(names)
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        elif command == "names":
            print(list(names))
        else:
            print("Whoops, that's not right!")
            help_info()

    filename = input('Enter a name for the output file, or \'no\' to not make one: ')
    if filename == 'no':
        exit(0)

    file = open(filename, 'w+')
    file.write('Pairings:\n')
    for pair in ship_dict:
        file.write(pair + " : " + ship_dict.get(pair) + "\n")
    file.write('\n')
    file.write('Roles:')
    for pair in role_dict:
        file.write(pair + " : " + ship_dict.get(pair) + "\n")


main()
