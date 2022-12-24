##### UNDERGROUND STORY LINES #####

import os
from player import my_player
from text import prompt_text

##### UNDERGROUND MAP #####
#Dictionary w/ nested distionary: stores each zone tile information
underground_map = {
    "a1": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "",
        "down": "a2",
        "left": "",
        "right": "b1"
    },
    "b1": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "",
        "down": "b2",
        "left": "a1",
        "right": "c1"
    },
    "c1": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "",
        "down": "c2",
        "left": "b1",
        "right": "d1"
    },
    "d1": {
        "zone": "Well",
        "inspect": "This is the Well!",
        "explored": False,
        "up": "",
        "down": "d2",
        "left": "c1",
        "right": "e1"
    },
    "e1": {
        "zone": "Sewer",
        "inspect": "This is the Sewer!",
        "explored": False,
        "up": "",
        "down": "e2",
        "left": "d1",
        "right": ""
    },
    "a2": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "a1",
        "down": "a3",
        "left": "",
        "right": "b2"
    },
    "b2": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "b1",
        "down": "b3",
        "left": "a2",
        "right": "c2"
    },
    "c2": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "c1",
        "down": "c3",
        "left": "b2",
        "right": "d2"
    },
    "d2": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "d1",
        "down": "d3",
        "left": "c2",
        "right": "e2"
    },
    "e2": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "e1",
        "down": "e3",
        "left": "d2",
        "right": ""
    },
    "a3": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "a2",
        "down": "a4",
        "left": "",
        "right": "b3"
    },
    "b3": {
        "zone": "Merchant",
        "inspect": "This is the merchant!",
        "explored": False,
        "up": "b2",
        "down": "b4",
        "left": "a3",
        "right": "c3"
    },
    "c3": {
        "zone": "Capital",
        "inspect": "This is the Capital!",
        "explored": False,
        "up": "c2",
        "down": "c4",
        "left": "b3",
        "right": "d3"
    },
    "d3": {
        "zone": "Square",
        "inspect": "This is the market square!",
        "explored": False,
        "up": "d2",
        "down": "d4",
        "left": "c3",
        "right": "e3"
    },
    "e3": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "e2",
        "down": "e4",
        "left": "d3",
        "right": ""
    },
    "a4": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "a3",
        "down": "a5",
        "left": "",
        "right": "b4"
    },
    "b4": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "b3",
        "down": "b5",
        "left": "a4",
        "right": "c4"
    },
    "c4": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "c3",
        "down": "c5",
        "left": "b4",
        "right": "d4"
    },
    "d4": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "d3",
        "down": "d5",
        "left": "c4",
        "right": "e4"
    },
    "e4": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "e3",
        "down": "e5",
        "left": "d4",
        "right": ""
    },
    "a5": {
        "zone": "Junk",
        "inspect": "This is the junk yard!",
        "explored": False,
        "up": "a4",
        "down": "",
        "left": "",
        "right": "b5"
    },
    "b5": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "b4",
        "down": "",
        "left": "a5",
        "right": "c5"
    },
    "c5": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "c4",
        "down": "",
        "left": "b5",
        "right": "d5"
    },
    "d5": {
        "zone": "Home",
        "inspect": "This is your Home!",
        "explored": True,
        "up": "d4",
        "down": "",
        "left": "c5",
        "right": "e5"
    },
    "e5": {
        "zone": "NA",
        "inspect": "",
        "explored": False,
        "up": "e4",
        "down": "",
        "left": "d5",
        "right": ""
    }
}     

def story():
    my_player.location = "d5"
    os.system("clear")
    background = f"You wake up at your home in the underground, your mom calls your name.\nMom: {my_player.name} can you run over to the market and pick up some rations and water for us?\nYou grab some tradeable items and head off to the market.\n"
    prompt_text(background)
    my_player.quest = "Get supplies from square."
