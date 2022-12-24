##### PLAYER SETUP AND CONTROLS #####

import os
from underground import underground_map
from player import my_player

##### MOVEMENT MECHANICS #####
def movement(direction):
    if(direction == "w" and underground_map[my_player.location]["up"] != ""):
        my_player.location = underground_map[my_player.location]["up"]
        underground_map[my_player.location]["explored"] = True
    elif(direction == "a" and underground_map[my_player.location]["left"] != ""):
        my_player.location = underground_map[my_player.location]["left"]
        underground_map[my_player.location]["explored"] = True
    elif(direction == "s" and underground_map[my_player.location]["down"] != ""):
        my_player.location = underground_map[my_player.location]["down"]
        underground_map[my_player.location]["explored"] = True
    elif(direction == "d" and underground_map[my_player.location]["right"] != ""):
        my_player.location = underground_map[my_player.location]["right"]
        underground_map[my_player.location]["explored"] = True
    else:
        print("Out of Bounds!")

def show_map():
    i = 0
    for key in underground_map.keys(): 
        i += 1
        if underground_map[key]["explored"]:
            print(underground_map[key]["zone"], end = " ")
        else:
            print("##", end = " ")
        if i == 5:
            print("\n")
            i = 0

def inspect():
    print(underground_map[my_player.location]["inspect"])

def quest():
    print(f"Current Quest: {my_player.quest}")

def hotkeys():
    while my_player.game_over is False:
        option = input("> ").lower()
        if option == "m":
            os.system("clear")
            show_map()
        elif option in ["w", "a", "s", "d"]:
            os.system("clear")
            movement(option)
        elif option == "i":
            os.system("clear")
            inspect()
        elif option == "q":
            quest()
        elif option == "h":
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
            print("- Type exit to resume")
            