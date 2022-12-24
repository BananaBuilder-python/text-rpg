##### TEXT RPG GAME #####

import sys
import os
from player_mechanics import movement, inspect, show_map, quest, hotkeys
from background import setup
from underground import story
from player import my_player

##### TITLE MENU #####
def title_menu_options():
    os.system("clear")
    print("#################################")
    print("##                             ##")
    print("##  Welcome to Cyber Text RPG  ##")
    print("##                             ##")
    print("#################################")
    print("            - Play -             ")
    print("            - Help -             ")
    print("            - More -             ")
    print("            - Quit -             ")
    while True:
        option = input("> ").lower()
        if option == "play":
            start_game()
            break
        elif option == "help":
            help_menu()
            break
        elif option == "more":
            more_menu()
            break
        elif option == "quit":
            sys.exit()
        else:
            print("Please type a valid command")
            
##### HELP SCREEN #####
def help_menu():
    os.system("clear")
    print("#################################")
    print("#            Help Menu          #")
    print("#################################")
    print("- Read carefully, and choose wisely")
    print("- Type your choice and click enter")
    print("- Type w, a, s, d to move in a direction")
    print("- Type m to view the map")
    print("- Type i to interact")
    print("- Type q to view active quest")
    print("- Good luck and have fun!")
    print("- Type exit to leave")
    while True:
        option = input("> ").lower()
        if option == "exit":
            title_menu_options()
            break
        else:
            print("Please type a valid command")

##### MORE MENU #####
def more_menu():
    os.system("clear")
    print("#################################")
    print("#            More Menu          #")
    print("#################################")
    print("- Hi everyone! My name is Andy")
    print("- This is my first pyhton project!")
    print("- I hope you enjoy it!")
    print("- Type exit to leave")
    while True:
        option = input("> ").lower()
        if option == "exit":
            title_menu_options()
            break
        else:
            print("Please type a valid command")

##### GAME FUNCTIONALITY #####
def start_game():
    setup()
    story()
    #hotkeys()

##### GAME START #####
title_menu_options()