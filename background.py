##### GAME BACKGROUND LORE FOR EACH STORY #####

import os
from text import prompt_text
from player import my_player

##### GAME SETUP #####
def setup():
    os.system("clear")
    name = "Hello, what's your name?\n"
    prompt_text(name)
    my_player.name = input("> ")
    instructions = f"Nice to meet you {my_player.name}! You can type 'h' at anytime to view the help menu. You can move useing the W, A, S, D keys. You can interact using I and view active quest anytime using q.\n"
    prompt_text(instructions)
    print("Which story line would you like to start with?")
    print("Underground, Wasteland, Jericho, Space")
    while True:
        origin = input("> ").lower()
        if origin in ["underground", "wasteland", "jericho", "space"]:
            my_player.origin = origin
            break
        else:
            print("Please chose a valid story")
    if my_player.origin == "underground":
        underground_lore()

##### UNDERGROUND START BACKGROUND #####
def underground_lore():
    lore = f"You live in the underground..."
    prompt_text(lore)
    os.system("clear")
    
    