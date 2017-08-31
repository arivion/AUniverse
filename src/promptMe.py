"""
:file: promptMe.py
An application to generate writing prompts


:author: Alexia Christie
"""

import characters
import random

names = ("Jack", "Lana", "Scott", "Mary", "Wren", "Alice",
                 "Elijah", "Claire", "Silas", "Emily", "Teddy", "Sam")


def tarot() -> str:
    card_number = random.randint(1, 78)
    if card_number > 56:
        card_name = "Major"
    else:
        card_name = "Minor"
    return card_name


def main():
    random.seed(None)
    auto = input("Run in universe mode? ").lower()
    if auto == "y" or auto == "yes":
        characters.manual()
    else:
        print("Focus character: " + names[random.randint(0, len(names)-1)])
        print("")


main()
