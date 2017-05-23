"""

"""
# TODO: name IO somehow (file/input options?)

import random


class Group:

    def __init__(self, name: str):
        self.name = name
        self.members = []

    def add_member(self, name: str):
        self.members.append(name)


def help_info():
    print("Usage:")
    print("\tships: pair up characters (with a chance of some being single)")
    print("\tchoose: pick a character at random")
    print("\tgroups: randomly assign characters to groups")
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


def group_up(names: tuple, groups: list, force: str):

    groups_list = []
    names_list = list(names)

    if force == "y" and len(names) < len(groups):
        choice = input("Cannot force one member per group." +
                       "Proceed anyway? [y/n]: ").lower()
        if choice == "n":
            return
        else:
            force = "n"

    for name in groups:
        groups_list.append(Group(name))

    if force == "y":
        for group in groups_list:
            name = names_list[random.randint(0, len(names_list)-1)]
            names_list.remove(name)
            group.add_member(name)
    for character in names_list:
        groups_list[random.randint(0, len(groups_list)-1)].add_member(character)
    for group in groups_list:
        print("Members of group " + group.name + ": ", end='')
        for character in group.members:
            print(character + " ", end='')
        print(" ")


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
        elif command == "groups":
            groups = input("Enter the names of the groups, separated by only commas:\n")
            groups = groups.split(",")
            force = input("Force at least one character per group? [y/n]: ").lower()
            group_up(names, groups, force)
        elif command == "choose":
            print(names[random.randint(0, len(names)-1)])
        else:
            print("Whoops, that's not right!")
            help_info()


main()
