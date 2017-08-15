"""
:file: promptMe.py
An application to generate writing prompts


:author: Alexia Christie
"""

import characters
import random

names = ("Jack", "Lana", "Scott", "Mary", "Wren", "Alice",
                 "Elijah", "Claire", "Silas", "Emily", "Teddy", "Sam")
settings = ("Steampunk", "Witcher")


def main():
    random.seed(None)
    auto = input("Run in manual mode? ").lower()
    if auto == "y" or auto == "yes":
        characters.manual()
    else:
        print("Focus character: " + names[random.randint(0, len(names)-1)])
        print("Setting: " + settings[random.randint(0, len(settings)-1)])



main()
