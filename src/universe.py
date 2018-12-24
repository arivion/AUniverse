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
    char_list = list(characters)
    pairs = len(char_list) // 2
    pair_map = {}

    while True:

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

        roll_again = input('Roll again? : ')
        if roll_again.lower() is 'y' or roll_again.lower() is 'yes':
            continue
        break

    return pair_map


def assign(characters: tuple):
    """
    Assigns characters to roles
    :param characters: a tuple containing the names of the characters
    :return: a dictionary mapping character:role
    """
    char_list = list(characters)
    role_map = {}

    print('Enter any roles that you want randomly assigned.')
    print('If there are more characters than roles, you will be given the option of manually setting roles'
          ' for those left over.')
    print('There are [' + str(len(characters)) + '] characters.')
    print('Enter roles here, separated by commas:')
    roles = input().split(',')

    while True:

        for role in roles:
            role.lstrip().rstrip()
            character = char_list[random.randint(0, len(char_list)-1)]
            role_map[character] = role
            char_list.remove(character)
            print(character + ' has the following role: ' + role)
            if not char_list:
                break

        for leftover_char in char_list:
            role = input('Assign a role for ' + leftover_char + ': ')
            role_map[leftover_char] = role

        roll_again = input('Roll again? : ')
        if roll_again.lower() is 'y' or roll_again.lower() is 'yes':
            continue
        break

    return role_map


def main():
    random.seed(None)

    names = tuple(input("Enter names separated by commas: ").split(","))
    for name in names:
        name.lstrip().rstrip()
    ship_dict = {}
    role_dict = {}

    while 1:
        command = input("> ").lower()
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


main()
