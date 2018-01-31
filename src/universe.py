"""
:file: characters.py
Application to help brainstorm character relationships and loyalties

:author: Alexia Christie
"""

import random


class Group:
    def __init__(self, name: str):
        """
        Creates a group object
        :param name: name of the group
        """
        self.name = name
        self.members = []

    def add_member(self, character: str):
        """
        Adds a member to a group
        :param character: the new member
        """
        self.members.append(character)

    def add_sub(self, subgroup: object):
        """
        Adds a subgroup
        :param subgroup: the group within the group
        """
        self.members.append(subgroup)


def help_info():
    """
    Print usage information to terminal
    :return: None
    """
    print("Usage:")
    print("  ships: pair up characters (with a chance of some being single)")
    print("  choose: pick a character at random")
    print("  groups: randomly assign characters to groups")
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
        # Display results, with a 10% chance of the characters both being single.
        if random.randint(0, 9) == 0:
            print(char + " is single.")
            print(partner + " is single.")
        else:
            print(char + " and " + partner + " are together.")
    if len(char_list) != 0:
        print(char_list[0] + " is single.")


def group_up(names: tuple, master: str, groups: list, force: str):
    """
    Puts characters into groups, and vice versa
    :param names: character names
    :param master: name of group category
    :param groups: groups
    :param force: whether to balance groups
    :return: None
    """
    main_group = Group(master)
    names_list = list(names)
    counter = 0
    for name in groups:
        main_group.add_sub(Group(name))
    for character in names_list:
        # TODO: fix known issue where, when num of groups would leave a remainder character, loop is infinite.
        while 1:
            group = main_group.members[random.randint(0, len(main_group.members)-1)]
            counter += 1
            # If balancing results, pick a different group if this one has enough.
            if (force == 'y' or force == 'yes') and len(group.members) >= (len(names) // len(groups)):
                continue
            break
        group.add_member(character)
    for group in main_group.members:
        print("  Members of group " + group.name + ": ", end='')
        for character in group.members:
            print(character + " ", end='')
        print(" ")


def main():
    random.seed(None)
    enter = input("Would you like to enter character names? [y/n]: ").lower()
    if enter == "y":
        names = tuple(input("Enter names separated by commas: ").split(", "))
    else:
        names = ("Jack", "Lana", "Scott", "Mary", "Wren", "Alice",
                 "Elijah", "Claire", "Silas", "Emily", "Teddy", "Sam")
    help_info()
    while 1:
        command = input("> ").lower()
        if command == "quit":
            break
        elif command == "help":
            help_info()
        elif command == "ships":
            shipping(tuple(names))
        elif command == "groups":
            group_cat = input("Enter group category (eg Careers, Class, Race, etc): ")
            groups = input("Enter the names of the groups, separated by commas:\n")
            groups = groups.split(", ")
            force = input("Attempt to Balance Groups? [y/n]: ").lower()
            group_up(names, group_cat, groups, force)
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        elif command == "names":
            print(list(names))
        else:
            print("Whoops, that's not right!")
            help_info()


main()