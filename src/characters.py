"""
:file: characters.py
Application to help brainstorm character relationships and loyalties

:author: Alexia Christie
"""
# TODO: file input, change set (overall and temporarily)
# TODO: function to get groups associated with one name
# TODO: characters are objects, allow use of subset of characters w/ certain traits
# TODO: (maybe store results of groups and be able to create groups from only that?)
# TODO: file OUTPUT too, jackass
# TODO: if there aren't enough groups to do one character each, just do max one per group
# TODO: make add_sub and add_member one function?

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


class Character:
    def __init__(self, name: str):
        """
        Creates a character
        :param name: name of the character
        """
        self.name = name
        self.partner = ""


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
        char = char_list[random.randint(0, len(char_list)-1)]
        char_list.remove(char)
        partner = char_list[random.randint(0, len(char_list)-1)]
        char_list.remove(partner)
        if random.randint(0, 9) == 0:
            print(char.name + " is single.")
            print(partner.name + " is single.")
            char.partner = None
            partner.partner = None
        else:
            print(char.name + " and " + partner.name + " are together.")
            char.partner = partner.name
            partner.partner = partner.name
    if len(char_list) != 0:
        print(char_list[0] + " is single.")


def group_up(names: tuple, master: str, groups: list, force: str):
    """
    Puts characters into groups, and vice versa
    :param names: character names
    :param master: name of group category
    :param groups: groups
    :param force: whether to force at least one per group
    :return: None
    """
    main_group = Group(master)
    names_list = list(names)
    if force == "y" and len(names) < len(groups):
        choice = input("Cannot force one member per group." +
                       " Proceed anyway? [y/n]: ").lower()
        if choice == "n":
            return
        else:
            force = "n"
    for name in groups:
        main_group.add_sub(Group(name))
    if force == "y":
        for group in main_group.members:
            name = names_list[random.randint(0, len(names_list)-1)]
            names_list.remove(name)
            group.add_member(name)
    for character in names_list:
        main_group.members[random.randint(0, len(main_group.members)-1)].add_member(character)
    for group in main_group.members:
        print("  Members of group " + group.name + ": ", end='')
        for character in group.members:
            print(character + " ", end='')
        print(" ")


def manual():
    random.seed(None)
    characters = []
    enter = input("Would you like to enter character names? [y/n]: ").lower()
    if enter == "y":
        names = tuple(input("Enter names separated by commas: ").split(", "))
    else:
        names = ("Jack", "Lana", "Scott", "Mary", "Wren", "Alice",
                 "Elijah", "Claire", "Silas", "Emily", "Teddy", "Sam")
    for name in names:
        characters.append(Character(name))
    help_info()
    while 1:
        command = input("> ").lower()
        if command == "quit":
            break
        elif command == "help":
            help_info()
        elif command == "ships":
            shipping(tuple(characters))
        elif command == "groups":
            group_cat = input("Enter group category (eg Careers, Class, Race, etc): ")
            groups = input("Enter the names of the groups, separated by commas:\n")
            groups = groups.split(", ")
            force = input("Force at least one character per group? [y/n]: ").lower()
            group_up(names, group_cat, groups, force)
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        elif command == "names":
            print(list(names))
        else:
            print("Whoops, that's not right!")
            help_info()

